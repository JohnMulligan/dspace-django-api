from django.db.models import Avg,Sum,Min,Max,Count,Q
import json
from django.core.management.base import BaseCommand, CommandError
import time
import os
import re
import requests
from subway_ads.settings import base_dspace_url
from ads.models import Place, Subject, MediaType, ProductCategory, ProductType, Advertisement

class Command(BaseCommand):
	help = 'there ain\'t no balm in gilead'
	def handle(self, *args, **options):
		
		advertisements=Advertisement.objects.all()
		
		print('deleting all advertisements')
		c=0
		for ad in advertisements:
			ad.delete()
			c+=1
		print('deleted',c,'advertisements')
		
		filenames=[i for i in os.listdir("scraper/outputs") if i.endswith('.json')]
		
		print('adding',len(filenames),'advertisements')
		
		#takes a string where one half is bracketed and the other is not
		## returns the bracketed and unbracketed values, stripped down
		def brackets(s):
# 			print(s)
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
		
		for f in filenames:
			d=open("scraper/outputs/"+f,"r")
			t=d.read()
			j=json.loads(t)
			metadata=j["metadata"]
			d.close()
			
			uid=f[:-5]
			dspace_item_uri=base_dspace_url+"items/"+uid
			dspace_iiif_uri=base_dspace_url+"server/iiif/"+uid+"/manifest"
			
			owning_collection_uuid=j['owning_collection_uuid']
			
			title=metadata.get("dc.title")
			if title is not None:
				title=title[0]['value']
			
			ad=Advertisement(
				title=title,
				dspace_uri=dspace_item_uri,
				dspace_iiif_uri=dspace_iiif_uri,
				uid=uid
			)
			ad.save()	
			
			dspace_mediatypes=metadata.get("dc.type.genre") or []
			django_mediatypes=MediaType.objects.all()
			#these come in the format: "newspapers [\u62a5\u7eb8]"
			for dspace_mediatype in dspace_mediatypes:
				value=dspace_mediatype['value']
				chinese,english=brackets(value)
				this_media_type=django_mediatypes.filter(name_CN=chinese,name_EN=english)
				if len(this_media_type) == 0:
					m=MediaType(name_CN=chinese,name_EN=english)
					m.save()
				else:
					m=this_media_type[0]
				ad.genre.add(m)
				ad.save()
			
			django_prodtypes=ProductType.objects.all()
			dspace_prodtypes=metadata.get("dc.subject.prodtype") or []
			#these are all in english (or null)
			for dspace_prodtype in dspace_prodtypes:
				value=dspace_prodtype.get('value')
				this_prod_type=django_prodtypes.filter(name_EN=value)
				if len(this_prod_type) == 0:
					p=ProductType(name_EN=value)
					p.save()
				else:
					p=this_prod_type[0]
				ad.prod_type.add(p)
				ad.save()
			
			item_prod_cats=[]
			django_prodcats=ProductCategory.objects.all()
			dspace_prodcats=metadata.get("dc.subject.prodcat") or []
			#these are all in english (or null)
			for dspace_prodcat in dspace_prodcats:
				value=dspace_prodcat.get('value')
				this_prod_cat=django_prodcats.filter(name_EN=value)
				if len(this_prod_cat)==0:
					pc=ProductCategory(name_EN=value)
					pc.save()
				else:
					pc=this_prod_cat[0]
				ad.prod_cat.add(pc)
				ad.save()
			
# 			dspace_subtitles=metadata.get("dc.title.subtitle") or []
# 			#the formatting on these is not standardized. needs a cleanup
#			#therefore going to hold off on doing this one
# 			for dspace_subtitle in dspace_subtitles:
# 				value=dspace_subtitle.get('value')
# 				english,chinese=brackets(value)
# 				


			issue_date=metadata.get("dc.date.issued") or []
			#for this we're just getting the year (only 2 entries have actual timestamps)
			if issue_date!=[]:
				issue_date=issue_date[0]['value']
				year=re.match("^[0-9]{4}",issue_date).group(0)
				if year is not None:
					year=int(year)
				ad.pub_year=year
				ad.save()
			
			django_places=Place.objects.all()
			dspace_places=metadata.get("dc.coverage.spatial") or []
			#places are all place names in English
			for dspace_place in dspace_places:
				placename=dspace_place.get('value')
				this_place=django_places.filter(name_EN=placename)
				if len(this_place)==0:
					pl=Place(name_EN=placename)
					pl.save()
				else:
					pl=this_place[0]
				ad.spatial_coverage.add(pl)
				ad.save()
			
			django_subjects=Subject.objects.all()
			dspace_subjects=metadata.get("dc.subject") or []
			#these are all in english, with the occasional entry having a hyphenated specification
			#e.g. "Domestic - Hong Kong"
			for dspace_subject in dspace_subjects:
				subjectname=dspace_subject.get('value')
				this_subject=django_subjects.filter(name_EN=subjectname)
				if len(this_subject)==0:
					ts=Subject(name_EN=subjectname)
					ts.save()
				else:
					ts=this_subject[0]
				ad.subject.add(ts)
				ad.save()