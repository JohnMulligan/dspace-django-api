import requests
import time
from env import *
from authenticate import xsrfreq,authenticate
import json
import sys

item_id=sys.argv[1]

auth_headers=authenticate()

resp=requests.request("GET",url=base_url+'core/items/'+item_id,headers=auth_headers)

print(json.dumps(json.loads(resp.text),indent=3))