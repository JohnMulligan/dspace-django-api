import requests
import time
from subway_ads.localsettings import *
import json
import sys
	
def xsrfreq(url,headers={}):
# 	print(url,headers)
	r=requests.request("POST",url=url,headers=headers,verify=cert)
# 	print(r.headers)
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
		rheaders=xsrfreq(base_dspace_api_url)
	#then authenticate
	url= base_dspace_api_url + "authn/login?user=%s&password=%s" %(user,password)
	rheaders=xsrfreq(url=url,headers=rheaders)
	return(rheaders)