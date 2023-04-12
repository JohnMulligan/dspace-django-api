# DSpace --> Django API project

This project is an attempt to interface with the DSpace 7 API for

1. Indexing existing DSpace data
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
* the legacy data is great but it needs cleaning and rearchitecturing
* when we're done with all of that
	* we need a better-looking front-end
	* but with the stability of DSpace's back-end

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
	
As of April 12, I'm just using SQLite and shipping it with this repo, so you don't *have* to run the db setup, but:

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

#### C1. Walk your DSpace server

NOTE: Along the way, it turns on IIIF for each targeted item it finds.

You capture:

* all the collections you've enumerated in localsettings
* all the parents of those collections, all the way up, building a tree
* n.b. my current field parsers were thrown together pretty fast, they need a refactor once we get the schema down

	docker exec -i dspace-django bash -c "python3.9 manage.py saveItemsInCollections"
	** with an optional start page argument if you leave off at any point, e.g.
	docker exec -i dspace-django bash -c "python3.9 manage.py saveItemsInCollections 1234"

#### C2. Check or update an individual object

	docker exec -i dspace-django bash -c "python3.9 manage.py fetchSingleItem ....."

The naming convention there could be improved on -- it allows you to:

* provide any fully-qualified entity on the DSpace API
* get back the json of it
* and with the option of updating it, e.g.

	docker exec -i dspace-django bash -c "python3.9 manage.py fetchSingleItem /collections/6b14674d-6173-4e99-a3f1-2460dd369ea9"
	docker exec -i dspace-django bash -c "python3.9 manage.py fetchSingleItem /items/d2c9722d-af15-4a36-a01c-c12338f26b47 True"
	docker exec -i dspace-django bash -c "python3.9 manage.py fetchSingleItem /collections"
	&c &c

There's also an importimages script that works with S3 and a pre-existing OCR outputs folder. But that was temporary, we want this to live in the cloud when we're done and need to figure out temporary file mounts.

---------

## Using your new Django API

April 12: I've now got Solr running and indexing every text field! Need to integrate this into a simple-search endpoint.

March 30: I'm including some assets that used to be sensitive.

Now that the test server has moved, there shouldn't be an issue with sharing them

* sqlite db from the November scrape
* auth token: 4cd80ea57fc54d041b7e794a9f62d5f9e309d961
* admin login (AT 127.0.0.1:8000/admin): jcm10 SUBWAY_ADS

### EXAMPLE REQUESTS

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
		
#### A. PAGINATED COLLECTION VIEW 

##### A1. REQUEST TO THE ITEM LIST

	var myHeaders = new Headers();
	myHeaders.append("Authorization", "Token 4cd80ea57fc54d041b7e794a9f62d5f9e309d961");

	var requestOptions = {
	  method: 'POST',
	  headers: myHeaders,
	  redirect: 'follow'
	};

	fetch("127.0.0.1:8000/advertisement/", requestOptions)
	  .then(response => response.text())
	  .then(result => console.log(result))
	  .catch(error => console.log('error', error));

##### A2. RESPONSE (PAGINATED LIST VIEW)

* LONG-FORM JSON ARRAY OF DICTIONARIES
* A HEADER TELLING ME THERE ARE 4520 RESULTS
* ONLY THE FIRST 12 ITEMS IN THIS FIRST PAGE
* DISPLAYING JUST ONE HERE:

    [    {
        "id": 9045,
        "owning_collection": null,
        "spatial_coverage": [
            {
                "id": 1,
                "name_EN": "Taipei",
                "name_CN": null,
                "latitude": null,
                "longitude": null
            }
        ],
        "subject": [
            {
                "id": 1,
                "name_EN": "People",
                "name_CN": null
            },
            {
                "id": 2,
                "name_EN": "Male",
                "name_CN": null
            },
            {
                "id": 3,
                "name_EN": "Female",
                "name_CN": null
            },
            {
                "id": 4,
                "name_EN": "Asian",
                "name_CN": null
            },
            {
                "id": 5,
                "name_EN": "Domestic",
                "name_CN": null
            }
        ],
        "genre": [
            {
                "id": 1,
                "name_EN": "newspapers",
                "name_CN": "报纸"
            },
            {
                "id": 2,
                "name_EN": "advertisements",
                "name_CN": "广告"
            }
        ],
        "prod_cat": [
            {
                "id": 1,
                "name_EN": "Public and Private Transportation",
                "name_CN": null
            }
        ],
        "prod_type": [
            {
                "id": 1,
                "name_EN": "Airline",
                "name_CN": null
            }
        ],
        "title": "Cathay Life Insurance , Life Link. Cathy Life.",
        "dspace_uri": "https://dspace-v2.rice.edu/items/c2e21445-8926-441a-9ee3-ada6f9a3251b",
        "dspace_iiif_uri": "https://dspace-v2.rice.edu/server/iiif/c2e21445-8926-441a-9ee3-ada6f9a3251b/manifest",
        "uid": "c2e21445-8926-441a-9ee3-ada6f9a3251b",
        "pub_year": 2002,
        "subtitle_EN": null,
        "subtitle_CN": null
    },,...]

#### B-C. AUTOCOMPLETE WORKFLOW (it works with Chinese characters, too!)

Here we play out a use of the autocomplete endpoint, which allows for rapid searching/filtering.

The user opens an autocomplete text box on the "Subject" field and starts typing ("asia"). They receive back a couple valid entries.

They then select one of those valid entries ("Nonasian"), and the list filters for entries matching that value.

##### B1. IN AN AUTOCOMPLETE BOX, I MAKE A REQUEST TO SEE WHAT THE VALID ENTRIES ARE FOR "asian" IN THE ENGLISH "subject" FIELD

	var myHeaders = new Headers();
	myHeaders.append("Authorization", "Token 4cd80ea57fc54d041b7e794a9f62d5f9e309d961");

	var formdata = new FormData();
	formdata.append("subject__name_EN", "asia");

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
				"Asian",
				"Nonasian"
			]
		],
		"total_results_count": 2326
	}

##### C1. I NOW FILTER FOR ITEMS WITH "Nonasian" AS ONE OF THE VALUES IN THEIR ENGLISH "SUBJECT" FIELD

	var myHeaders = new Headers();
	myHeaders.append("Authorization", "Token 4cd80ea57fc54d041b7e794a9f62d5f9e309d961");

	var formdata = new FormData();
	formdata.append("subject__name_EN", "Nonasian");

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
* A HEADER TELLING ME THERE ARE 743 RESULTS
* ONLY THE FIRST 12 ITEMS IN THIS FIRST PAGE
* DISPLAYING JUST ONE HERE:

    [{
        "id": 9046,
        "owning_collection": null,
        "spatial_coverage": [
            {
                "id": 2,
                "name_EN": "Shanghai",
                "name_CN": null,
                "latitude": null,
                "longitude": null
            }
        ],
        "subject": [
            {
                "id": 1,
                "name_EN": "People",
                "name_CN": null
            },
            {
                "id": 2,
                "name_EN": "Male",
                "name_CN": null
            },
            {
                "id": 3,
                "name_EN": "Female",
                "name_CN": null
            },
            {
                "id": 6,
                "name_EN": "Nonasian",
                "name_CN": null
            },
            {
                "id": 7,
                "name_EN": "Foreign",
                "name_CN": null
            }
        ],
        "genre": [
            {
                "id": 1,
                "name_EN": "newspapers",
                "name_CN": "报纸"
            },
            {
                "id": 2,
                "name_EN": "advertisements",
                "name_CN": "广告"
            }
        ],
        "prod_cat": [
            {
                "id": 2,
                "name_EN": "Media and Information Technology",
                "name_CN": null
            }
        ],
        "prod_type": [
            {
                "id": 2,
                "name_EN": "Telecom",
                "name_CN": null
            }
        ],
        "title": "Xelibri Cell Phone, Xelibri. www.xelibri.com",
        "dspace_uri": "https://dspace-v2.rice.edu/items/4235780e-77be-4056-bcc3-2cb3ee680a70",
        "dspace_iiif_uri": "https://dspace-v2.rice.edu/server/iiif/4235780e-77be-4056-bcc3-2cb3ee680a70/manifest",
        "uid": "4235780e-77be-4056-bcc3-2cb3ee680a70",
        "pub_year": 2003,
        "subtitle_EN": null,
        "subtitle_CN": null
    },...]


------------

## April 12 notes on Data....

Broadly speaking, the project needs metadata standards and decisions about 

Because not only do we need new entries to fit DSpace standards -- it appears we also need to bring the existing records up to those standards as well.

Some examples follow.

### Field-splitting (existing records)

Chinese and English are currently mashed together in the same field.

We need to disaggregate these and then tag them properly.

We should also consider using the 'authority' field here to denote what data comes from the images and which are tags layered by Brendan on top of them.

E.G.,
	
	https://dspacedev.rice.edu/items/08929a0d-0ce4-409a-bf11-66b2ca69d8b7
	
	"dc.subject": [
		 {
			"value": "Picture[\u5b9e\u7269\u63d2\u56fe/\u60c5\u5883\u63d2\u56fe]",
			"language": null,
			"authority": null,
			"confidence": -1,
			"place": 0
		 },
		 ...
	 ]
         
	--SHOULD BE--
	
	"dc.subject": [
		 {
			"value": "Picture",
			"language": "English",
			"authority": null,
			"confidence": -1,
			"place": 0
		 },
		 "value": "\u5b9e\u7269\u63d2\u56fe/\u60c5\u5883\u63d2\u56fe",
			"language": "Chinese",
			"authority": null,
			"confidence": -1,
			"place": 0
		 },
		 ...
	]

I've performed this for the "Subjects" alias "Keywords" fields, but similar mashing is happening in Title, Place, and maybe other fields.

### Multilingual fields

Many advertisements contain both English and Chinese

Possible convention(s)

1. Provide full-English & full-Chinese translation alongside original, and tag these with "English" and "Chinese" lanaguages
1. Leave the language field null on the original? Or tag it as multilingual?
	
### Transcriptions, Descriptions, Full-Text Descriptions

Existing entries often have "Full-Text Description" and "Description"

What fields will we be using for actual transcriptions, and what for more editorial description?

### Media

* media per item
	* I'm only handling one image per item right now. But it looks like that might have to change -- I see some newspaper ads showing verso/recto
	* https://dspacedev.rice.edu/items/00352389-3a09-4a00-afa2-50ae91b48b66