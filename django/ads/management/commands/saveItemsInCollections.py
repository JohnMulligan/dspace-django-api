import requests
import json
from django.core.management.base import BaseCommand, CommandError
from ads.serializers import *
from ads.models import *
import time
from subway_ads.localsettings import *
from .tools.authenticate import authenticate
from .tools import local_items
from tools.nest import getornone
from .enable_iiif_on_items import enable_iiif

class Command(BaseCommand):
	
	'''
	
	This script
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
		
		def getpage(url):
			auth_headers=authenticate()
			resp=requests.request("GET",url=url,headers=auth_headers,verify=cert)
			try:
				j=json.loads(resp.text)
				nextpage=j['_links'].get('next')
				return j,nextpage
			except:
				print("request error",resp,auth_headers,url)
				return None,None

		def getsingle(url):
			auth_headers=authenticate()
			resp=requests.request("GET",url=url,headers=auth_headers,verify=cert)
			if resp.status_code==200:
				return 200,json.loads(resp.text)
			else:
				if resp.status_code!=204:
					print("request error",resp,auth_headers)
				return resp.status_code,None
		auth_headers=authenticate()
	
		#hit the items endpoint to get the firt page from the iterator
		first_url= base_dspace_api_url + "core/items"
		first_page,next_page=getpage(first_url)

		#print first page data
		page_meta=first_page['page']
		print(page_meta['totalElements'],'results =',page_meta['totalPages'],'pages at',page_meta['size'],'per page')
		
		startpage=options['startpage']
		next_page['href']=re.sub("(?<=page=)[0-9]+",str(startpage),next_page['href'])
		
		errorcount=0
		max_errors=50

		backofffactor=1
		backoff=10
		
		while next_page is not None:
			try:
				next_url=next_page['href']
				item_page,next_page=getpage(next_url)
				pagenumber=item_page['page']['number']
				print("page",pagenumber,next_url)
				try:
					for item in item_page['_embedded']['items']:
						item_uuid=item.get('uuid')
						item_name=item.get('name')
						print("-->",item_name,item_uuid)
						owning_collection_href=item['_links']['owningCollection']['href']
						sc,owning_collection_json=getsingle(owning_collection_href)
						owning_collection_uuid=owning_collection_json.get('uuid')
						if owning_collection_uuid in targeted_collections_uuids:
							uid=owning_collection_uuid
							name=owning_collection_json['name']
							uri=owning_collection_json['_links']['self']['href']
							owning_collection,owning_collection_isnew=Collection.objects.get_or_create(
								uid=uid,
								name=name,
								dspace_uri=uri
							)
							if owning_collection_isnew:
								print("owning collection is new:",uid,name,uri)
								this_collection=owning_collection
								parent_collection_href=owning_collection_json['_links']['parentCommunity']['href']
								bottomparentisfound=False
								while not bottomparentisfound and errorcount <= max_errors:		
									sc,parent_collection_dspace_json=getsingle(parent_collection_href)
									if sc==204:
										bottomparentisfound=True
										print('found top of tree')
									elif sc==200:
										name=parent_collection_dspace_json['name']
										uid=parent_collection_dspace_json['uuid']
										href=parent_collection_dspace_json['_links']['self']['href']
										print('new parent collection:',uid,name,href)
										parent_collection,parent_collection_isnew=Collection.objects.get_or_create(
											uid=uid,
											name=name,
											dspace_uri=href
										)
										this_collection.parent_collection=parent_collection
										this_collection.save()
										if not parent_collection_isnew:
											bottomparentisfound=True
										else:
											this_collection=parent_collection
											parent_collection_href=parent_collection_dspace_json['_links']['parentCommunity']['href']
									else:
										errorcount+=1
										print("error fetching",parent_collection_href,sc,"error count at",errorcount)
							local_items.create_or_update_item_from_json(item,owning_collection_uuid)
							ad=Advertisement.objects.get(uid=item_uuid)
							if not ad.iiif_enabled:
								resp=enable_iiif(item_uuid,auth_headers)
								if resp.status_code==200:
									ad.iiif_enabled=True
									ad.save()
									print("iiif enabled on",item_uuid)
								else:
									print("error enabling iiif on",item_uuid)
							else:
								print("iiif already enabled on",item_uuid)
				except:
					backofffactor=backoff*backofffactor
					auth_headers=authenticate()
			except:
				backofffactor=backoff*backofffactor
				auth_headers=authenticate()
				if errorcount<=max_errors:
					errorcount+=1
					print("ERROR. SKIPPING PAGE:",pagenumber)
					pagenumber+=1
					next_page['href']=re.sub("(?<=page=)[0-9]+",str(pagenumber),next_page['href'])
					print(next_page)
				else:
					print("ERROR: too many errors. quitting")
					exit()
				time.sleep(backofffactor)