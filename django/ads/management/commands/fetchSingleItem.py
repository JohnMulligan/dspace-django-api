import requests
import json
from django.core.management.base import BaseCommand, CommandError
from ads.serializers import *
from ads.models import *
import time
from subway_ads.localsettings import *
from tools.authenticate import xsrfreq,authenticate

class Command(BaseCommand):
	help = 'rebuilds the options flatfiles'
	def handle(self, *args, **options):
		#Here we define the output filenames
		# & the base serializer & object class we're feeding into it.
		item_id='0ac11e2f-d825-407b-84ee-a3c18b5b7685'
		print(item_id)
		auth_headers=authenticate()
		resp=requests.request("GET",url=base_dspace_api_url+'core/items/'+item_id,headers=auth_headers,verify=cert)
		print(json.dumps(json.loads(resp.text),indent=3))