import requests
import json
from subway_ads.localsettings import *
from .authenticate import authenticate

def enable_iiif(item_id):
	auth_headers=authenticate()
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
		url=base_url+'core/items/'+item_id,
		headers=headers,
		data=json.dumps(data),
		verify=cert
	)
	return(resp)

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