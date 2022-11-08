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

Easy :) --> https://github.com/rice-crc/voyages-api#using-the-api