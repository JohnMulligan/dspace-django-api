from django.db.models import Avg,Sum,Min,Max,Count,Q
from django.core.management.base import BaseCommand, CommandError
import time
import os
import re
from ads.models import *
import requests
import json
from subway_ads.localsettings import *

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
			
def create_or_update_item_from_json(item,owning_collection_uuid):
	owning_collection=Collection.objects.all().get_or_create(uid=owning_collection_uuid)
	metadata=item.get('metadata')
	uuid=item.get('uuid')
	name=item.get('name')
	dspace_item_uri=base_dspace_iiif_url+"items/"+uuid
	dspace_iiif_uri=base_dspace_iiif_url+uuid+"/manifest"
	title=metadata.get("dc.title")
	if title is not None:
		title=title[0]['value']
	ad,ad_isnew=Advertisement.objects.get_or_create(uid=uuid)
	if not ad.is_current or ad_isnew:
		ad.title=title
		ad.dspace_uri=dspace_item_uri
		ad.dspace_iiif_uri=dspace_iiif_uri
		ad.is_current=True
		ad.save()
	
		dspace_mediatypes=metadata.get("dc.type.genre") or []
		#these come in the format: "newspapers [\u62a5\u7eb8]"
		for dspace_mediatype in dspace_mediatypes:
			value=dspace_mediatype['value']
			if value is not None:
				chinese,english=brackets(value)
				this_media_type,this_media_type_isnew=MediaType.objects.all().get_or_create(name_CN=chinese,name_EN=english)
				this_media_type.save()
				ad.genre.add(this_media_type)
				ad.save()
	
		dspace_prodtypes=metadata.get("dc.subject.prodtype") or []
		#these are all in english (or null)
		for dspace_prodtype in dspace_prodtypes:
			value=dspace_prodtype.get('value')
			if value is not None:
				this_prod_type,this_prod_type_isnew=ProductType.objects.all().get_or_create(name_EN=value)
				ad.prod_type.add(this_prod_type)
				ad.save()
				this_prod_type.save()
	
		dspace_prodcats=metadata.get("dc.subject.prodcat") or []
		#these are all in english (or null)
		for dspace_prodcat in dspace_prodcats:
			value=dspace_prodcat.get('value')
			if value is not None:
				this_prod_cat,this_prod_cat_isnew=ProductCategory.objects.all().get_or_create(name_EN=value)
				ad.prod_cat.add(this_prod_cat)
				ad.save()
				this_prod_cat.save()

		issue_date=metadata.get("dc.date.issued") or []
		#for this we're just getting the year (only 2 entries have actual timestamps)
		if issue_date!=[]:
			issue_date=issue_date[0]['value']
			year=re.match("^[0-9]{4}",issue_date).group(0)
			if year is not None:
				year=int(year)
				ad.pub_year=year
				ad.save()
	
		dspace_places=metadata.get("dc.coverage.spatial") or []
		#places are all place names in English
		for dspace_place in dspace_places:
			value=dspace_place.get('value')
			if value is not None:
				this_place,this_place_isnew=Place.objects.all().get_or_create(name_EN=value)
				ad.spatial_coverage.add(this_place)
				ad.save()
				this_place.save()
	
		dspace_subjects=metadata.get("dc.subject") or []
		#these are all in english, with the occasional entry having a hyphenated specification
		#e.g. "Domestic - Hong Kong"
		for dspace_subject in dspace_subjects:
			value=dspace_subject.get('value')
			if value is not None:
				this_subject,this_subject_isnew=Subject.objects.all().get_or_create(name_EN=value)
				ad.subject.add(this_subject)
				ad.save()
		if ad_isnew:
			print("ad created",dspace_item_uri,dspace_iiif_uri)
		else:
			print("ad updated",dspace_item_uri,dspace_iiif_uri)
		
	else:
		print("ad is current",ad,ad.uid)