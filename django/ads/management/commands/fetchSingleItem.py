import requests
import json
from django.core.management.base import BaseCommand, CommandError
from ads.serializers import *
from ads.models import *
import time
from subway_ads.localsettings import *
from .tools.authenticate import authenticate
from .tools.update_local_item import *

class Command(BaseCommand):
	help = 'rebuilds the options flatfiles'

	def add_arguments(self, parser):
		parser.add_argument(
			"endpoint",
			type=str,
			nargs='?',
			default=None,
			help="api endpoint"
		)

		parser.add_argument(
			"update",
			type=bool,
			nargs='?',
			default=False,
			help="update true or false"
		)

	def handle(self, *args, **options):
		#Here we define the output filenames
		# & the base serializer & object class we're feeding into it.
		auth_headers=authenticate()
		
		endpoint=options['endpoint']
		
		if endpoint is not None:
			endpoint='/'+endpoint
		else:
			endpoint=''
				
		concat_url=base_dspace_api_url + endpoint
		
		print("-------------\nfetching url\n",concat_url,"\n--------------")

		resp=requests.request("GET",url=concat_url,headers=auth_headers,verify=cert)
		print(resp)
		if resp.status_code == 200:
			print(json.dumps(json.loads(resp.text),indent=3))
		
			print(options['update'])
		
			if options['update']:
				update_item_from_dspace_json(json.loads(resp.text),auth_headers)
			