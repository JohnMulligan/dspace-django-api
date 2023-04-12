import requests
import json
from subway_ads.localsettings import *
from ads.models import *
from .authenticate import authenticate

max_errors=2

def enable_iiif(item_id,auth_headers):
	errorcount=0
	print('enabling iiif')
	while errorcount<=max_errors:
		headers=auth_headers
		data=[{
			"path":"/metadata/dspace.iiif.enabled",
			"value":[{
					"value": True,
					"language": None,
					"authority": None,
					"confidence": -1,
					"place": 0
				}],
			"op":"add"
			}]
		headers.update({"content-type": "application/json", "accept": "application/json"})
		resp=requests.request(
			"PATCH",
			url=base_dspace_api_url+'core/items/'+item_id,
			headers=headers,
			data=json.dumps(data),
			verify=cert
		)
		if resp.status_code==200:
			return(resp)
		else:
			errorcount+=1
			auth_headers=authenticate()
			print(resp.status_code,"error enabling iiif. re-authenticating & retrying:",errorcount)
	raise ValueError('iiif enabling failed')

def getpage(url,auth_headers):
	errorcount=0
	while errorcount<=max_errors:
		resp=requests.request("GET",url=url,headers=auth_headers,verify=cert)
		if resp.status_code==200:
			try:
				j=json.loads(resp.text)
			except:
				print("response was:",resp,resp.text)
				raise ValueError('failed to parse response')
			nextpage=j['_links'].get('next')
			return j,nextpage
		else:
			errorcount+=1
			auth_headers=authenticate()
			print(resp.status_code,"error getting dspace page. re-authenticating & retrying:",errorcount)
	raise ValueError('failed to get page')

def getsingle(url,auth_headers):
	errorcount=0
	while errorcount<=max_errors:
		resp=requests.request("GET",url=url,headers=auth_headers,verify=cert)
		if resp.status_code==200:
			try:
				j=json.loads(resp.text)
			except:
				raise ValueError('failed to parse response')
			return 200,json.loads(resp.text)
		elif resp.status_code==204:
			return resp.status_code,None
		else:
			errorcount+=1
			auth_headers=authenticate()
			print(resp.status_code,"error getting item. re-authenticating & retrying:",errorcount)
	raise ValueError('iiif enabling failed')