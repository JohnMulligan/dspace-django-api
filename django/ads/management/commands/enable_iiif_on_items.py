import requests
import json
from subway_ads.localsettings import *
from .tools.authenticate import authenticate
from django.core.management.base import BaseCommand, CommandError
from ads.models import *

def enable_iiif(item_id,auth_headers):
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
		url=base_dspace_api_url+'core/items/'+item_id,
		headers=headers,
		data=json.dumps(data),
		verify=cert
	)
	print(resp)
	return(resp)

class Command(BaseCommand):
	help = 'rebuilds the options flatfiles'
	def handle(self, *args, **options):
		
		advertisements=Advertisement.objects.all()
		auth_headers=authenticate()
		
		for ad in advertisements:
			uid=ad.uid
			resp=enable_iiif(uid,auth_headers)
			print(resp,uid)
			if resp.status_code!=200:
				success=False
				errors=1
				errorlimit=5
				while errors <=errorlimit:
					auth_headers=authenticate()
					resp=enable_iiif(uid,auth_headers)
					if resp.status_code!=200:
						errors+=1
					print(resp,uid)
				if errors==errorlimit:
					print('item failed, moving on',uuid)