import requests
import json
from django.core.management.base import BaseCommand, CommandError
from ads.serializers import *
from ads.models import *
import time
from subway_ads.localsettings import *
from .tools.authenticate import authenticate
from .tools import local_items
from .tools import remote_items
from tools.nest import getornone

class Command(BaseCommand):
	help = 'rebuilds the options flatfiles'
	def handle(self, *args, **options):

		def getpage(url):
			auth_headers=authenticate()
			resp=requests.request("GET",url=url,headers=auth_headers,verify=cert)
			try:
				j=json.loads(resp.text)
				nextpage=j['_links'].get('next')
				return j,nextpage
			except:
				print("request error",resp)
				return None,None

		def getsingle(url):
			auth_headers=authenticate()
			resp=requests.request("GET",url=url,headers=auth_headers,verify=cert)
			j=json.loads(resp.text)
			return j

		#Here we define the output filenames
		# & the base serializer & object class we're feeding into it.
# 		item_id='0ac11e2f-d825-407b-84ee-a3c18b5b7685'
# 		print(item_id)
		auth_headers=authenticate()
# 		resp=requests.request("GET",url=base_dspace_api_url+'core/items/'+item_id,headers=auth_headers,verify=cert)
# 		print(json.dumps(json.loads(resp.text),indent=3))
	
		#hit the items endpoint to get the firt page from the iterator
		first_url= base_dspace_api_url + "core/items"
		first_page,next_page=getpage(first_url)

		#print first page data
		page_meta=first_page['page']
		print(page_meta['totalElements'],'results =',page_meta['totalPages'],'pages at',page_meta['size'],'per page')

# 		if startpage is not None:
# 			next_page['href']=re.sub("(?<=page=)[0-9]+",str(startpage),next_page['href'])
# 
# 		if results_per_page is not None:
# 			next_page['href']=re.sub("(?<=size=)[0-9]+",str(results_per_page),next_page['href'])

		errorcount=0
		max_errors=50

		backofffactor=1
		backoff=10
		
		while next_page is not None:
# 			try:
			next_url=next_page['href']
			item_page,next_page=getpage(next_url)
			pagenumber=item_page['page']['number']
			print("page",pagenumber,next_url)

# 			try:
			for item in item_page['_embedded']['items']:
				item_uuid=item.get('uuid')
				item_name=item.get('name')
				print("-->",item_name,item_uuid)
				
				
				owning_collection_href=item['_links']['owningCollection']['href']
				
				owning_collection=getsingle(owning_collection_href)
				owning_collection_uuid=owning_collection.get('uuid')
				if owning_collection_uuid in targeted_collections_uuids:
					local_items.create_or_update_item_from_json(item,owning_collection_uuid)
# 				else:
# 					print("no owning collection for item",item_uuid,item_name)
# 			except:
# 				print("ERROR: no items in",url)
# 				backofffactor=backoff*backofffactor
# 				auth_headers=authenticate()
# 				errorcount+=1
# 				time.sleep(backofffactor)
# 			except:
# 				backofffactor=backoff*backofffactor
# 				auth_headers=authenticate()
# 				if errorcount<=max_errors:
# 					errorcount+=1
# 					print("ERROR: UNKNOWN. SKIPPING PAGE:",pagenumber)
# 					pagenumber+=1
# 					next_page['href']=re.sub("(?<=page=)[0-9]+",str(pagenumber),next_page['href'])
# 					print(next_page)
# 				else:
# 					print("ERROR: too many errors. quitting")
# 					exit()
# 				time.sleep(backofffactor)