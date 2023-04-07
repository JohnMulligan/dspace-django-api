import requests
import time
from env import *
from authenticate import xsrfreq,authenticate
import json
import sys
import os

auth_headers=authenticate()

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

filenames=[i for i in os.listdir("outputs") if i.endswith('.json')]

headers=auth_headers
headers.update({"content-type": "application/json", "accept": "application/json"})

for f in filenames:
	item_id=f[:-5]
	resp=requests.request(
		"PATCH",
		url=base_url+'core/items/'+item_id,
		headers=headers,
		data=json.dumps(data)
	)
	print(item_id,resp)