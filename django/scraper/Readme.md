# python scripts for scraping dspace 

* env.py --> used by all of the below to store credentials and uuids where necessary
* authenticate.py --> used by all of the below to authenticate.
* saveItemsInCollections.py PAGENUMBER
	* given collection ids stored in env.py
	* walks through those collections and pulls all their items
	* saves their json representations in outputs folder
	* ... because in DSpace, you can see
		* what "owningcollection" an item belongs to
		* but not what items are owned by such an "owningcollection"
		* n.b. this isn't the case for non-owning collections -- those work as one would expect
	* because the server sometimes bonks, and this script gives up after 5 errors
		* you may want to specify the page you'd like to start on if you're resuming
		* optional arg is, therefore, a page integer / checkpoint
		* items that have already been gathered will simply be overwritten
		* so it's a good idea to go back a page or two to ensure coverage
* fetchSingleItem.py ITEMID --> pull info on a single item by its uuid
* enableiiif_allitems_inoutputfolder.py --> walks through the filenames in outputs folder, turns on iiif for all of them by uuid


n.b. the outputs folder is in gitignore, so your work will only be saved locally