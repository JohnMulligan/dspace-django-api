import requests
import time
from env import *
from authenticate import xsrfreq,authenticate
import json
import sys
import re
import time

try:
	startpage=sys.argv[1]
except:
	startpage=None
	
try:
	results_per_page=sys.argv[2]
except:
	results_per_page=30

auth_headers=authenticate()

def getpage(url):
	global auth_headers
	resp=requests.request("GET",url=url,headers=auth_headers)
	try:
		j=json.loads(resp.text)
		nextpage=j['_links'].get('next')
		return j,nextpage
	except:
		print("request error",resp)
		return None

def getsingle(url):
	global auth_headers
	resp=requests.request("GET",url=url,headers=auth_headers)
	j=json.loads(resp.text)
	return j
	
#hit the items endpoint to get the firt page from the iterator
first_url= base_url + "core/items"
first_page,next_page=getpage(first_url)

#print first page data
page_meta=first_page['page']
print(page_meta['totalElements'],'results =',page_meta['totalPages'],'pages at',page_meta['size'],'per page')

if startpage is not None:
	next_page['href']=re.sub("(?<=page=)[0-9]+",str(startpage),next_page['href'])

if results_per_page is not None:
	next_page['href']=re.sub("(?<=size=)[0-9]+",str(results_per_page),next_page['href'])

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
				try:
					uuid=item['uuid']
					name=item['name']
					metadata=item['metadata']
					try:
						owning_collection_href=item['_links']['owningCollection']['href']
						owning_collection=getsingle(owning_collection_href)
						owning_collection_uuid=owning_collection['uuid']
						if owning_collection_uuid in desired_collections_uuids:
							output_dict={
								'metadata':metadata,
								'owning_collection_uuid':owning_collection_uuid
							}
							d=open('outputs/'+uuid+'.json','w')
							d.write(json.dumps(output_dict))
							print('match:',uuid,name)
					except:
						print("ERROR: no owning connection for",item)
						errorcount+=1
						time.sleep(2)
				except:
					print("ERROR: item lacks basic metadata",item)
					errorcount+=1
					time.sleep(2)
		except:
			print("ERROR: no items in",url)
			backofffactor=backoff*backofffactor
			auth_headers=authenticate()
			errorcount+=1
			time.sleep(backofffactor)
	except:
		backofffactor=backoff*backofffactor
		auth_headers=authenticate()
		if errorcount<=max_errors:
			errorcount+=1
			print("ERROR: UNKNOWN. SKIPPING PAGE:",pagenumber)
			pagenumber+=1
			next_page['href']=re.sub("(?<=page=)[0-9]+",str(pagenumber),next_page['href'])
			print(next_page)
		else:
			print("ERROR: too many errors. quitting")
			exit()
		time.sleep(backofffactor)