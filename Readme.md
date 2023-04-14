# DSpace --> Django API project

This project prototypes an interface between Django and the DSpace 7 API for

1. Indexing existing DSpace data
1. Ingesting data from other sources
1. Providing a staging ground for users to
	1. clean existing data
	1. create new data
1. Writing back to DSpace
1. Re-present indexed data back out via a DRF REST API
1. Making use of
	1. Solr via django-haystack
	1. IIIF via DSpace 7
	1. S3 storage for the new images and data to be staged
	1. External OCR services for auto-transcription

Our use-case here is
	
* we've got a legacy collection in DSpace
* there are thousands of photos that haven't been included yet
* the legacy data is great but it needs cleaning and restructuring
* when we're done with all of that, we need:
	* a better-looking front-end (React)
	* a reliable REST API to serve data to that front-end (Django middleman)
	* a IIIF server (Dspace 7!)
	* a permanent, standards-based home for the cleaned data (Dspace)
	
[I've sketched an architecture for this setup here.](Proposed_Architecture.pdf)

## Setup

### A. Docker and conf files

You'll need the following files for this project to run:

* DSpace chain.pem & .crt certs
* Localsettings with the appropriate variables set (see localsettings.py-example)
* R/W access to an S3 bucket

Then you should be able to just build the container: ```docker-compose --build```

	n.b. there is some architectural work to be done in the docker-compose file
		-- had to hack the solr build to make it django 4.0 compatible
		-- the certs setup was a little too bespoke due to docker oddities

### Initial django setup

	docker exec -i dspace-django bash -c "python3.9 manage.py collectstatic"
	
As of April 14, I stopped shiping the SQLite db with this repo. Email JCM10 for these files.

Still running it in SQLite to keep it portable while we iterate.

	docker exec -i dspace-django bash -c "python3.9 manage.py makemigrations"
	docker exec -i dspace-django bash -c "python3.9 manage.py migrate"
	docker exec -i dspace-django bash -c "python3.9 manage.py createsuperuser <yourusername>"

### B. Solr

Field indexing templated: ads/templates/search/indexes/ads/advertisement_text.txt

	docker exec -i dspace-django-solr solr delete -c dspace
	docker exec -i dspace-django-solr solr create -c dspace
	docker exec -i dspace-django bash -c "python3.9 manage.py build_solr_schema" --configure-directory=./"
	mv django/*.xml solr/
	docker exec -i dspace-django-solr sh -c "cp /srv/dspace-django/solr/schema.xml /var/solr/data/dspace/conf"
	docker restart dspace-django-solr
	docker exec -i dspace-django bash -c "python3.9 manage.py rebuild_index --noinput"

### C. Custom management commands

#### C0. Generate a templated schema

I refactored the entire schema on a templated basis on April 13 because it was clear that my field mappings across the several collections weren't capturing the extensive and rich metadata.

The templating script a little hidebound right now. It assumes:

1. That there is *one* abstract model base class (though you can tweak it after the fact of course)
1. That there is *one* field that all of the captured metadata is being piped into
1. That the relationship of these entities we're creating is many-to-many.

So it works best with controlled vocabularies within the specified ontologies.

It retrieves sample items specified by the user, pulls all the metadata field names, and cobbles them together into the elements needed for a pretty robust data capture.

You run the templater by feeding it sample uuid's.

	docker exec -i dspace-django /bin/bash -c "python3.9 manage.py dspace_template_django --item_uuid='08929a0d-0ce4-409a-bf11-66b2ca69d8b7,00b1c5ba-8610-4105-b1e7-f4c9c5eef009'"

#### C1. Walk your DSpace server

NOTE: Along the way, it turns on IIIF for each targeted item it finds.

You capture:

* all the collections you've enumerated in localsettings
* all the parents of those collections, all the way up, building a tree
* n.b. my current field parsers were thrown together pretty fast, they need a refactor once we get the schema down

e.g.

	docker exec -i dspace-django bash -c "python3.9 manage.py saveItemsInCollections"
	** with an optional start page argument if you leave off at any point, e.g.
	docker exec -i dspace-django bash -c "python3.9 manage.py saveItemsInCollections 1234"

#### C2. Check or update an individual object

	docker exec -i dspace-django bash -c "python3.9 manage.py fetchSingleItem ....."

The naming convention there could be improved on -- it allows you to:

* provide any fully-qualified entity on the DSpace API
* get back the json of it
* and with the option of updating it

e.g.

	docker exec -i dspace-django bash -c "python3.9 manage.py fetchSingleItem --path='collections/6b14674d-6173-4e99-a3f1-2460dd369ea9'""
	docker exec -i dspace-django bash -c "python3.9 manage.py fetchSingleItem --path='items/d2c9722d-af15-4a36-a01c-c12338f26b47' --update=True"
	docker exec -i dspace-django bash -c "python3.9 manage.py fetchSingleItem --path='collections'"

There's also an importimages script that works with S3 and a pre-existing OCR outputs folder. But that was temporary, we want this to live in the cloud when we're done and need to figure out temporary file mounts.

---------

## Using your new Django API

April 12: I've now got Solr running and indexing every text field! Need to integrate this into a simple-search endpoint.

March 30: I'm including some assets that used to be sensitive.

Now that the test server has moved, there shouldn't be an issue with sharing them

* sqlite db from the November scrape
* auth token: 4cd80ea57fc54d041b7e794a9f62d5f9e309d961
* admin login (AT 127.0.0.1:8000/admin): jcm10 SUBWAY_ADS2023

### EXAMPLE REQUESTS

* Introduction: OPTIONS
* A. basic collection view
	* Request the items page
	* Receive
		* the first 12 items (helps w/ thumbnail image layout)
		* Including a IIIF manifest pointer
		* and a header telling me there are 4520 total results
* B-C. autocomplete filtering workflow
	* B1. Request all listings in the English "subject" field that contain "asian"
	* B2. Find that there are 2 genres with that substring:
		* "Asian"
		* "Nonasian"
	* C1. Request the items page *with a filter* of subject__name_EN="Nonasian"
	* C2. Receive
		* the first 12 items including a IIIF manifest pointer
		* and a header telling me there are 743 total results
		
#### INTRODUCTION: OPTIONS

The "options" request to the main endpoint we have here exposes the django ORM. It's generated automatically.

Interfaces can use this to structure their requests to the filter interfaces, as described in the examples that follow.

We're using the same basic logic as in the new Voyages API & React UI prototypes.

OPTIONS REQUEST:

	var myHeaders = new Headers();
	myHeaders.append("Authorization", "Token .....");

	var formdata = new FormData();

	var requestOptions = {
	  method: 'OPTIONS',
	  headers: myHeaders,
	  body: formdata,
	  redirect: 'follow'
	};

	fetch("127.0.0.1:8000/advertisement/", requestOptions)
	  .then(response => response.text())
	  .then(result => console.log(result))
	  .catch(error => console.log('error', error));

OPTIONS RESPONSE:

	{
		"id": {
			"type": "<class 'rest_framework.fields.IntegerField'>",
			"label": "ID",
			"flatlabel": "ID"
		},
		"chao_date_chineselunars": {
			"type": "table",
			"label": "chao.date.chineselunar",
			"flatlabel": "chao.date.chineselunar",
			"id": {
				"type": "<class 'rest_framework.fields.IntegerField'>",
				"label": "ID",
				"flatlabel": "chao.date.chineselunar : ID"
			},
			"text_original": {
				"type": "<class 'rest_framework.fields.CharField'>",
				"label": "Text original",
				"flatlabel": "chao.date.chineselunar : Text original"
			},
			"text_EN": {
				"type": "<class 'rest_framework.fields.CharField'>",
				"label": "Text EN",
				"flatlabel": "chao.date.chineselunar : Text EN"
			},
			"text_CN": {
				"type": "<class 'rest_framework.fields.CharField'>",
				"label": "Text CN",
				"flatlabel": "chao.date.chineselunar : Text CN"
			}
		},
		
		...
		
	}

So what follows is some examples of how to build requests based on the above structure.

#### A. PAGINATED COLLECTION VIEW 

##### A1. REQUEST TO THE ITEM LIST

	var myHeaders = new Headers();
	myHeaders.append("Authorization", "Token .....");

	var formdata = new FormData();

	var requestOptions = {
	  method: 'POST',
	  headers: myHeaders,
	  body: formdata,
	  redirect: 'follow'
	};

	fetch("127.0.0.1:8000/advertisement/", requestOptions)
	  .then(response => response.text())
	  .then(result => console.log(result))
	  .catch(error => console.log('error', error));

##### A2. RESPONSE (PAGINATED LIST VIEW)

* LONG-FORM JSON ARRAY OF DICTIONARIES
* A HEADER TELLING ME THERE ARE  RESULTS
* ONLY THE FIRST 12 ITEMS IN THIS FIRST PAGE

SAMPLE:

	[
		{
			"id": 1,
			"chao_date_chineselunars": [],
			"chao_company_addresss": [],
			"chao_company_names": [
				{
					"id": 1,
					"text_original": "兰勃脱白脱勒公司[Sphinx]",
					"text_EN": null,
					"text_CN": null
				}
			],
			"chao_company_nations": [
				{
					"id": 1,
					"text_original": "U.S.A.[美國]",
					"text_EN": null,
					"text_CN": null
				}
			],
			...
		},
		...
	]
		
#### B-C. AUTOCOMPLETE WORKFLOW (it works with Chinese characters, too!)

Here we play out a use of the autocomplete endpoint, which allows for rapid searching/filtering.

The user opens an autocomplete text box on the "Subject" field and starts typing ("asia"). They receive back a couple valid entries.

They then select one of those valid entries ("Nonasian"), and the list filters for entries matching that value.

##### B1. IN AN AUTOCOMPLETE BOX, I MAKE A REQUEST TO SEE WHAT THE VALID ENTRIES ARE FOR "le" IN THE "subject" RAW TEXT FIELD

	var myHeaders = new Headers();
	myHeaders.append("Authorization", "Token .....");

	var formdata = new FormData();
	formdata.append("dc_subjects__text_original", "le");

	var requestOptions = {
	  method: 'POST',
	  headers: myHeaders,
	  body: formdata,
	  redirect: 'follow'
	};

	fetch("127.0.0.1:8000/advertisement/autocomplete", requestOptions)
	  .then(response => response.text())
	  .then(result => console.log(result))
	  .catch(error => console.log('error', error));

##### B2. RESPONSE: ALL THE DB's IEXACT MATCHES ON TITLE FIELD

	{
		"results": [
			[
				"Female",
				"Female[女性]",
				"Male",
				"Male[男性]",
				"Middle age",
				"Middle age People[中年人]",
				"Middle age people[中年人]",
				"Middle age people[青年人]",
				"Motor vehicles, trailers and semi-trailers",
				"Old people[老年人]",
				"People",
				"Radio, television and communication equipment and apparatus[廣播電視通訊設備及部件]",
				"Young people[青年人]",
				"old people[老年人]",
				"people[中年人]",
				"女性[Female]",
				"电子配件[Electronic accessories]"
			]
		],
		"total_results_count": 7942
	}

##### C1. THE USER NOW CLICKS A COUPLE ENTRIES IN THE AUTOCOMPLETE BOX.

I NOW RUN THESE 2 SELECTED VALUES ON THE SAME FIELD AS EXACT MATCHES ON THE advertisement ENDPOINT:

	var myHeaders = new Headers();
	myHeaders.append("Authorization", "Token .....");

	var formdata = new FormData();
	formdata.append("dc_subjects__text_original", "Motor vehicles, trailers and semi-trailers");
	formdata.append("dc_subjects__text_original", "Middle age People[中年人]");

	var requestOptions = {
	  method: 'POST',
	  headers: myHeaders,
	  body: formdata,
	  redirect: 'follow'
	};

	fetch("127.0.0.1:8000/advertisement/", requestOptions)
	  .then(response => response.text())
	  .then(result => console.log(result))
	  .catch(error => console.log('error', error));

##### C2. RESPONSE  (PAGINATED LIST VIEW)

* LONG-FORM JSON ARRAY OF DICTIONARIES
* A HEADER TELLING ME THERE ARE 238 RESULTS
* ONLY THE FIRST 12 ITEMS IN THIS FIRST PAGE

Sample from the top of the first item:

	[
		{
			"id": 45,
			"chao_date_chineselunars": [],
			"chao_company_addresss": [],
			"chao_company_names": [
				{
					"id": 4,
					"text_original": "第威德制藥公司[E.G. DeWitt & CO.]",
					"text_EN": null,
					"text_CN": null
				}
			],
			"chao_company_nations": [
				{
					"id": 1,
					"text_original": "U.S.A.[美國]",
					"text_EN": null,
					"text_CN": null
				}
			],
			"chao_contributor_printers": [
				{
					"id": 1,
					"text_original": "Press of Hankow Times[汉口中西报社]",
					"text_EN": null,
					"text_CN": null
				}
			],
			"chao_date_minguos": [
				{
					"id": 14,
					"text_original": "中华民国二十二年七月十五日",
					"text_EN": null,
					"text_CN": null
				}
			],
			...
		},
		...
	]


##### D. SOLR

This one's in process. But you can see it working in the django shell:

	#enter the django ubuntu 20 container
	docker exec -it dspace-django /bin/bash
	
	#enter the django/python shell
	python3.9 manage.py shell
	
	#following the the solr example here: https://django-haystack.readthedocs.io/en/latest/searchqueryset_api.html#quick-start
	>>> from haystack.query import SearchQuerySet
	>>> all_results = SearchQuerySet().all()
	>>> len(all_results)
	6194
	>>> beautyset=all_results.filter(content='beauty')
	>>> len(beautyset)
	80
	>>> from ads.models import PublishedAdvertisement
	>>> ad=PublishedAdvertisement.objects.get(id=beautyset[0].pk[0])
	>>> ad
	<PublishedAdvertisement: SOCIE Beauty Salon Sogo Department , SOCIE>
	# to see how much data solr is storing on each item, hit:
	>>> beautyset[0].__dict__

------------

## THE DATA QUESTION (April 12-14)

1. We are now capturing an enormous amount of rather heterogeneous data
	1. 44 fields from DSpace across 2 ontologies:
		1. Dublin Core
		1. Chao
	1. My semi-automated templating scripts did all that, missing only 2 fields:
		1. 'chao.company.otherinfo'
		1. 'dc.relation'
	1. The best part is that it maps *directly* back to the ontologies named above
	1. So that is very good but...
1. You have 2 core types of item now. which share those 44 fields:
	1. *Staged Item*, whose extra data is:
		1. Connection to S3 objects (secure, scalable access from anywhere)
		1. Edited or not edited
		1. Approved or not
	1. Published Item, whose extra data is:
		1. DSpace Unique Universal Identifier
		1. DSpace URI
		1. DSpace IIIF manifest address
1. We also have some *powerful* built-in functionality, though it needs iteration
	1. Solr full-text search across all of your fields for single-search functionality
	1. JCM's API endpoints, plugged into the Published Advertisements:
		1. An options endpoint that describes the full schema (auto-generated)
		1. In process: a universal search across all text fields backed by Solr
		1. Basic text search for short fields, enabling autocomplete filter components
		1. Numeric-handling endpoint, enabling rangeslider filter components
	1. Inexact search on any individual field
1. What code haven't we written yet?
	1. Pull from JStor
	1. Publication from Django to DSpace
	1. A well-though-out editorial workflow for the above
	1. Infrastructural changes for production vs. staging deployment
		1. this is VERY important. in our setup, the app has write access to DSpace
		1. so we probably want SSO *and* a only have that access on a firewalled instance
	1. Secure authentication method (Rice SSO) -- I've implemented this elsewhere though
	1. React front-end app -- though we have prototype components
	1. Custom views (e.g. transcriptions) for when the admin interface doesn't cut it
1. JCM made some design decisions here
	1. DSpace will be our source of authority
		1. All the data cleaning and entry will happen in Django
		1. We won't publish any Advertisement data that's not in DSpace
		1. That doesn't exclude having essays/blog posts that gather items together
	1. All ingested data goes to a "text_original" field
	1. So now *every* metadata entry has two empty fields:
		1. "text_CN"
		1. "text_EN"
	1. Which pushes us towards a setup like the following:
		1. dc.subject: {value:"Japan[日本]"} becomes...
			1. dc.subject : {value:"Japan",lang:"English"} 
			1. dc.subject : {value:"日本",lang:"Chinese"}
	1. My only customization was to hand-tune certain fields for long text
	1. And I'm not accounting for other kinds of data types
		1. Integers (e.g., "publication year")
		1. Full dates (like "publication date")
		1. Geo data (like "spatial extent")
	1. All Dublin Core & Chao data allow for multiple entries
1. Rather than hand-tuning any further, we need to take a step back and ask:
	1. What fields do you want to ultimately be using in your archive?
	1. What data do you want to be using in those fields?
	1. What are the optimal editorial interfaces for doing the following:
		1. Reviewing existing and "cleaned" data
		1. Planning or executing batch cleaning jobs like
			1. Merging duplicate items or fields
			1. Splitting mashed items or fields
		1. Interfacing with complex data for cleaning in an efficient way
			1. Transcription correction
			1. others?
	1. To what extent do you want, for batch cleaning jobs:
		1. Automated:
			1. this costs lots of $$ for programming...
			1. but could benefit others
		1. Bespoke:
			1. this costs less $$ in theory...
			1. but you have to either
				1. sit down with a programmer and do it carefully and review
				1. learn to do it yourself
			1. so in this framework there's an implicit cost:
				1. you spend until you're out of programmer time
				1. and then the metadata batch jobs are done
	1. To what extent do you want to automate metadata generation?
		1. OCR (Ying's Microsoft job was excellent. Let's stick with that service.)
		1. Entity recognition? https://github.com/distant-viewing/dvt
	1. How do we want to fold in the other items:
		1. Hard disk photos (and what data do we capture)
		1. JStor forums items
			1. how do we get that data?
			1. how will we map those fields to your Chao & DC ontologies on ingest?
	1. Can you quantify, for planning purposes:
		1. Existing photos in DSpace (I count 6194)
		1. Existing photos in JStor Forums/ArtStor
		1. Offline photos (hard disks, google drive, etc.) (and approx. total size)
		1. Time (approx.) it takes you to hand-edit a staged item in the current admin UI
1. We also need to articulate some end-user experience questions.
	1. What do your visitors see when they get to the site?
	1. How do they search for content?
	1. Do we need to record any metadata that doesn't fit in DSpace? (RECOMMEND AGAINST.)