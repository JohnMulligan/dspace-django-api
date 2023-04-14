from django.db.models import Avg,Sum,Min,Max,Count,Q
from django.core.management.base import BaseCommand, CommandError
import time
import os
import re
from ads.models import *
import requests
import json
from subway_ads.localsettings import *
from . import remote_items
from ads.dspace_term_model_map import term_to_model

def brackets(s):
	bracketed=re.search("(?<=\[).*?(?=\])",s)
	if bracketed is not None:
		bracketed=bracketed.group(0)
		s2=re.sub("\["+re.escape(bracketed)+"\]","",s)
		bracketed=bracketed.strip()
		s=s2.strip()
	unbracketed=s
	if unbracketed=="":
		unbracketed=None
	return bracketed,unbracketed

#this parses the item json and updates them locally
def create_or_update_item_from_json(item):
	metadata=item.get('metadata')
	uuid=item.get('uuid')
	name=item.get('name')
	dspace_item_uri=base_dspace_items_url+uuid
	dspace_iiif_uri=base_dspace_iiif_url+uuid+"/manifest"
	title=metadata.get("dc.title")
	if title is not None:
		title=title[0]['value']
	ad,ad_isnew=PublishedAdvertisement.objects.get_or_create(uuid=uuid)
	if ad_isnew or not ad.is_current:
		ad.dspace_uri=dspace_item_uri
		ad.dspace_iiif_uri=dspace_iiif_uri
		ad.is_current=True
		ad.save()
		
		for term in metadata:
			
			modellookup=term_to_model.get(term)
			if modellookup is not None:
				modelname=modellookup['classname']
				model=eval(modelname)
				termname=modellookup['related_name']
			
				for entry in metadata[term]:
					value=entry['value']
					this_model_object,this_model_object_isnew=model.objects.get_or_create(
						text_original=value
					)
					this_model_object.save()
					eval('ad.%s.add(this_model_object)' %termname)
					ad.save()
			else:
				print("THIS FIELD IS NOT MAPPED-->",term)
		
		dspace_subjects=metadata.get("dc.subject") or []
# PREVIOUSLY I WAS PARSING THE FIELDS INTO EN & CN entries -- but there's too much variety now that I'm capturing over a dozen fields.
# WE'LL HAVE TO BUILD AFTER-THE-FACT PARSING/CLEANING SCRIPTS AFTER SOME DELIBERATION.
#these are all in english, with the occasional entry having a hyphenated specification
#e.g. "Domestic - Hong Kong"
# 		for dspace_subject in dspace_subjects:
# 			value=dspace_subject.get('value')
# 			print(value)
# 			if value is not None:
# 				#some of these are formatted like: 'Picture[实物插图/情境插图]'
# 				#in which case:
# 				subject_EN=re.search("[^[]*",value)
# 				subject_CN=re.search("(?<=\[)[^]]*",value)
# 				if subject_EN and subject_CN:
# 					this_subject,this_subject_isnew=Subject.objects.all().get_or_create(
# 						name_CN=subject_CN.group(0),
# 						name_EN=subject_EN.group(0)
# 					)
# 					ad.subjects.add(this_subject)
# 					ad.save()
# 				#others like: "Domestic - Hong Kong"
# 				else:
# 					this_subject,this_subject_isnew=Subject.objects.all().get_or_create(name_EN=value)
# 					ad.subjects.add(this_subject)
# 					ad.save()
		if ad_isnew:
			print("ad created",dspace_item_uri,dspace_iiif_uri)
		else:
			print("ad updated",dspace_item_uri,dspace_iiif_uri)
	else:
		print("ad is current",ad,ad.uuid)
	return ad


def update_collections_tree(owning_collection_json,auth_headers):
	owning_collection_uuid=owning_collection_json['uuid']
	name=owning_collection_json['name']
	uri=owning_collection_json['_links']['self']['href']
	owning_collection,owning_collection_isnew=Collection.objects.get_or_create(
		uid=owning_collection_uuid,
		name=name,
		dspace_uri=uri
	)
	if owning_collection_isnew:
		errorcount=0
		max_errors=5
		print("owning collection is new:",owning_collection_uuid,name,uri)
		this_collection=owning_collection
		parent_collection_href=owning_collection_json['_links']['parentCommunity']['href']
		bottomparentisfound=False
		while not bottomparentisfound and errorcount <= max_errors:		
			sc,parent_collection_dspace_json=remote_items.getsingle(parent_collection_href,auth_headers)
			if sc==204:
				bottomparentisfound=True
				print('found top of tree')
			elif sc==200:
				name=parent_collection_dspace_json['name']
				uid=parent_collection_dspace_json['uuid']
				href=parent_collection_dspace_json['_links']['self']['href']
				print('new parent collection:',uid,name,href)
				parent_collection,parent_collection_isnew=Collection.objects.get_or_create(
					uid=uid,
					name=name,
					dspace_uri=href
				)
				this_collection.parent_collection=parent_collection
				this_collection.save()
				if not parent_collection_isnew:
					bottomparentisfound=True
				else:
					this_collection=parent_collection
					parent_collection_href=parent_collection_dspace_json['_links']['parentCommunity']['href']
			else:
				errorcount+=1
				auth_headers=authenticate
				print("reauthenticating: error fetching",parent_collection_href,sc,"error count at",errorcount)
		if errorcount>=max_errors:
			print('collection creation failed')
			raise ValueError('collection creation failed')
	return owning_collection,auth_headers

##this takes dspace item json
###and handles the interfacing with the remote items
###and hands off to collection and item creators
###then attaches the item to its collection
def update_item_from_dspace_json(item,auth_headers):
	item_uuid=item.get('uuid')
	item_name=item.get('name')
	print("-->",item_name,item_uuid)
	owning_collection_href=item['_links']['owningCollection']['href']
	sc,owning_collection_json=remote_items.getsingle(owning_collection_href,auth_headers)
	owning_collection_uuid=owning_collection_json.get('uuid')
	if owning_collection_uuid in targeted_collections_uuids:
		ad=create_or_update_item_from_json(item)
		owning_collection,auth_headers=update_collections_tree(owning_collection_json,auth_headers)
		ad.owning_collection=owning_collection
		ad.save()
		return ad,auth_headers
	else:
		return None,auth_headers