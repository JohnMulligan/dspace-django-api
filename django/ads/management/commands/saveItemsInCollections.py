import requests
import json
import re
from django.core.management.base import BaseCommand, CommandError
from ads.models import *
import time
from subway_ads.localsettings import *
from .tools.authenticate import authenticate
from .tools import remote_items
from .tools import local_items

max_errors=5

class Command(BaseCommand):
	
	'''
	
	This script (and those it hands off to)
	1. walks through all the items in the dspace server/api/core/items endpoint
	2. identifies those items that belong to the collections we are targeting
	3. pulls their basic metadata and writes it to the db
	3a. updating the item if it already exists -- unless the item is already flagged as is_current (boolean for now, could be more robust based on updated timestamps)
	3b. creating the item if it does not
	4. 	enabling iiif if the local db determines has it flagged as not enabled
	
	'''
	
	def add_arguments(self, parser):
		parser.add_argument(
			"startpage",
			type=int,
			nargs='?',
			default=1,
			help="begin at a particular page in the items list -- good for checkpointing."
		)

	def handle(self, *args, **options):
		
		auth_headers=authenticate()
	
		#hit the items endpoint to get the firt page from the iterator
		first_url= base_dspace_api_url + "core/items"
		first_page,next_page=remote_items.getpage(first_url,auth_headers)

		#print first page data
		page_meta=first_page['page']
		print(page_meta['totalElements'],'results =',page_meta['totalPages'],'pages at',page_meta['size'],'per page')
		
		startpage=options['startpage']
		next_page['href']=re.sub("(?<=page=)[0-9]+",str(startpage),next_page['href'])
		
		errorcount=0
		max_errors=5
		
		while next_page is not None:
			next_url=next_page['href']
			item_page,next_page=remote_items.getpage(next_url,auth_headers)
			pagenumber=item_page['page']['number']
			print("page",pagenumber,next_url)
			
			for item_json in item_page['_embedded']['items']:
				ad=local_items.update_item_from_dspace_json(item_json,auth_headers)
				#the above function returns an ad if it's in the collections we're looking for
				#if not, it returns None
				if ad is not None:
					if not ad.iiif_enabled:
						resp=remote_items.enable_iiif(ad.uid,auth_headers)
						if resp.status_code==200:
							print('iiif enabled')
						else:
							print('error enabling iiif',resp,ad)
					else:
						print('iiif already enabled')
						
						
						
						