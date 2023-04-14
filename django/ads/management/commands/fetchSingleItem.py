import requests
import json
from django.core.management.base import BaseCommand, CommandError
from ads.serializers import *
from ads.models import *
import time
from subway_ads.localsettings import *
from .tools.authenticate import authenticate
from .tools.local_items import *

class Command(BaseCommand):
	help = 'pulls the json for a single dspace entity'

	def add_arguments(self, parser):
		parser.add_argument(
			"--path",
			type=str,
			nargs='?',
			default='',
			help="Str: the fully-qualified path off the api endpoint, eg 'items/d2c9722d-af15-4a36-a01c-c12338f26b47' or just 'collections'"
		)

		parser.add_argument(
			"--update",
			type=bool,
			nargs='?',
			default=False,
			help="Boolean: update the item you're pinging. default=False"
		)

	def handle(self, *args, **options):
		#Here we define the output filenames
		# & the base serializer & object class we're feeding into it.
		auth_headers=authenticate()
		
		path=options['path']
		
		if path is not None:
			path='core/'+path
		else:
			path=''
				
		concat_url=base_dspace_api_url + path
		
		print("-------------\nfetching url\n",concat_url,"\n--------------")

		resp=requests.request("GET",url=concat_url,headers=auth_headers,verify=cert)
		print(resp)
		if resp.status_code == 200:
			print(json.dumps(json.loads(resp.text),indent=3))
		
			print(options['update'])
		
			if options['update']:
				update_item_from_dspace_json(json.loads(resp.text),auth_headers)
			