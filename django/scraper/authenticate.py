import requests
import time
from env import *
import json
import sys
	
def xsrfreq(url,headers={}):
	print(url,headers)
	r=requests.request("POST",url=url,headers=headers)
	print(r.headers)
	if 'DSPACE-XSRF-TOKEN' in r.headers:
		dxtoken=r.headers['DSPACE-XSRF-TOKEN']
	else:
		dxtoken=headers['X-XSRF-TOKEN']
	cookie="DSPACE-XSRF-COOKIE=%s" %dxtoken
	rheaders={'X-XSRF-TOKEN':dxtoken,'Cookie':cookie}
	if 'Authorization' in r.headers:
		rheaders['Authorization']=r.headers['Authorization']
	return rheaders

def authenticate(rheaders=None):
	#first get a prelim auth token
	if rheaders is None:
		rheaders=xsrfreq(base_url)
	#then authenticate
	url= base_url + "authn/login?user=%s&password=%s" %(user,password)
	rheaders=xsrfreq(url=url,headers=rheaders)
	return(rheaders)

if __name__=="__main__":
	url=reslource_id=sys.argv[1]

	auth_headers=authenticate()

	resp=requests.request("GET",url=url,headers=auth_headers)

	print(json.dumps(json.loads(resp.text),indent=3))