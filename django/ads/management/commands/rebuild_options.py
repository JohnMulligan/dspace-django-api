import requests
import json
from django.core.management.base import BaseCommand, CommandError
from ads.serializers import AdvertisementSerializer
from ads.models import *

class Command(BaseCommand):
	help = 'rebuilds the options flatfiles'
	def handle(self, *args, **options):
		#Here we define the output filenames
		# & the base serializer & object class we're feeding into it.
		 
		flatfile_params=[
			{
				'output_filename':'ads/advertisement_options.json',
				'serializer':AdvertisementSerializer,
				'objectclass':Advertisement
			}
		]

		def addlevel(thisdict,keychain,payload):
			thiskey=keychain.pop(0)
			if len(keychain)>0:
				if thiskey not in thisdict:
					thisdict[thiskey]={}
				thisdict[thiskey]=addlevel(thisdict[thiskey],keychain,payload)
			else:
				if thiskey not in thisdict:
					thisdict[thiskey]=payload
				else:
					if type(payload)==dict:
						for p in payload:
							thisdict[thiskey][p]=payload[p]
			return thisdict

		def valuesconcatenate(valuelist,joiner):
			joinedlabel=joiner.join([i for i in valuelist if i not in [None,'']])
			return(joinedlabel)

		def options_walker2(schema,base_address,serializer,baseflatlabel=None):
			try:
				fields=serializer.fields
			except:
				fields=serializer.child.fields
			for field in fields:
				datatypestr=str(type(fields[field]))
				if base_address!='':
					address='__'.join([base_address,field])
				else:
					address=field
				if 'serializer' in datatypestr:
					#print(address,datatypestr)
					if 'ListSerializer' in datatypestr:
						#this gets the table label from m2m connections on reverse/related field lookups
						try:
							label=serializer.fields[field].child.Meta.model._meta.verbose_name
						except:
							label=serializer.child[field].__dict__['_field'].__dict__['label']
					else:						
						try:
							label=serializer.child.fields[field].Meta.model._meta.verbose_name
						except:
							try:
								label=serializer.Meta.model.__dict__[field].__dict__['field'].__dict__['related_query_name']
							except:
								label=serializer.Meta.model.__dict__[field].__dict__['field'].__dict__['verbose_name']
							
					flatlabel=valuesconcatenate([baseflatlabel,label]," : ")
					schema[address]={'type':'table','label':label,'flatlabel':flatlabel}
					#schema[address]={'type':'table','label':label}
					schema=options_walker2(schema,address,fields[field],flatlabel)
				else:
					try:
						label=fields[field].__dict__['label']
					except:
						label=fields[field].__dict__['verbose_name']
					flatlabel=valuesconcatenate([baseflatlabel,label]," : ")
					schema[address]={'type':datatypestr,'label':label,'flatlabel':flatlabel}
					#schema[address]={'type':datatypestr,'label':label}
			return schema
		
		for fp in flatfile_params:
			output_filename=fp['output_filename']
			serializer=fp['serializer']
			objectclass=fp['objectclass']
			print("options for %s" %str(serializer))
			testobject=objectclass.objects.all()
			testobject=serializer(testobject,many=False)
			flat=options_walker2({},'',testobject)
			d=open(output_filename,'w')
			d.write(json.dumps(flat,indent=2))
			d.close
			print("--> wrote %d var descriptions"%len(flat))