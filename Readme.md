# DSpace --> Django API project

This project is an attempt to

* interface with the DSpace 7 API
* allowing Django to capture its data
* and represent that data via a DRF API
* ... for the use of a IIIF React document viewer app

In other words, we scrape DSpace to put its data in an easier-to-use API that can be searched by external apps.

For this project, I'm re-using much of the code from voyages-api.

Down the line, we might be able to do away with the Django middleman.

## Scraping DSpace

For now, we're doing this outside of Django but I'd like to integrate it soon under advertisement/management/commands

In the "scraper" subfolder you will find

* env_example.py
	* rename that to env.py
	* fill in your DSpace API credentials
	* add the uuid's of the collections you want to capture
* saveItemsInCollection.py
	* run this to capture all the data in the collections specified in env.py
	* they'll be dumped as json files with the uuid's as their filenames in outputs/
* enableiiif_allitems_inoutputfolder.py
	* if iiif is not enabled on those items, you can run this to switch it on
	* it uses the filenames in outputs/ to build its uri's for its PATCH calls

... a little more documentation in that folder

## Building the django app

### 1. Set up the environment:

	cd subway_ads/
	python3 -m venv venv
	source venv/bin/activate
	pip3 install -r requirements.txt

### 2A. If you have a db, put it in this folder alongside manage.py, requirements.txt, etc.

### 2B. If you *don't* have a db to work with:

Build it like this:

	python3 manage.py makemigrations
	python3 manage.py migrate

Then import your records like this:

	python3 manage.py import_records.py

... this is where I will eventually integrate the scraping into the django app. currently, i'm capturing only the following fields, and in a pretty unsophisticated manner: 

	dc.title
	dc.type.genre
	dc.subject.prodtype
	dc.subject.prodcat
	dc.title.subtitle
	dc.date.issued
	dc.coverage.spatial
	dc.subject

### 3. Launch the app

	python3 manage.py runserver

## Using your new Django API

For March 30, I'm including some assets that used to be sensitive.

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
	