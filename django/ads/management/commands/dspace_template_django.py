import requests
import json
from django.core.management.base import BaseCommand, CommandError
from ads.models import *
import time
from subway_ads.localsettings import *
from .tools.authenticate import authenticate

def make_camelcase_name(s):
	s=s.lower()
	sparts=s.split('.')
	camelcasename=''
	for spart in sparts:
		camelcasename+=spart.title()
	return camelcasename
	
class Command(BaseCommand):
	help = 'spits out templated django models and admins'

	def add_arguments(self, parser):
		parser.add_argument(
			"--item_uuids",
			type=str,
			nargs='?',
			default=None,
			help="Comma-delimited Str:item uuid:the item that we will be templating off of"
		)
		parser.add_argument(
			"--base_class_name",
			type=str,
			nargs='?',
			default='BilingualShortFieldAbstractBase',
			help="Str: The name of the abstract base class these are templated of of"
		)
		parser.add_argument(
			"--target_app_name",
			type=str,
			nargs='?',
			default='ads',
			help="Str: The name of the app we're targeting"
		)
		
		parser.add_argument(
			"--target_class_name",
			type=str,
			nargs='?',
			default='Advertisement',
			help="Str: The name of the class that all these templated fields will be pointing at"
		)
		
	def handle(self, *args, **options):
		
# APR 13 SAMPLE ITEMS
# 		39665b64-6cd6-4928-9f19-4d9cd80638f1
# 		08929a0d-0ce4-409a-bf11-66b2ca69d8b7
# 		dfc47062-7f05-477e-b81a-d1502ad3a5d5
# 		117f6ceb-bc4e-4d8d-b2ea-1a0693fcd40a
# 		81cb15a4-6a9d-4fbf-88e8-f25af77270a0
# 		8dda18f5-b2ce-42a3-a557-b95ab25e3ed9
# 		e95b7ce0-0a20-4702-ad17-957d09b25325

#Here we define the output filenames
# & the base serializer & object class we're feeding into it.
		
		auth_headers=authenticate()
		
		item_uuids=options['item_uuids']
		
		target_class_name=options['target_class_name']
		
		base_class_name=options['base_class_name']
		
		target_app_name=options['target_app_name']
		
		admin_inlines=[]
		class_models=[]
		target_class_fields=[]
		target_admin_inlines_entries=[]
		admin_registrations=[]
		serializers=[]
		nestedserializerlines=[]
		
		targetmodelprefixes=["Published","Staged"]
		solrblocks={prefix:[] for prefix in targetmodelprefixes}
		
		term_model_dict={}
		
		
		
		for item_uuid in item_uuids.split(','):
			concat_url=base_dspace_api_url + 'core/items/' + item_uuid
		
			print("-------------\nfetching url\n",concat_url,"\n--------------")

			resp=requests.request("GET",url=concat_url,headers=auth_headers,verify=cert)
			print(resp)
		

			if resp.status_code == 200:
				sampleitem=json.loads(resp.text)
				print(json.dumps(sampleitem,indent=3))
			
				metadata=sampleitem['metadata']
			

				for targetmodelprefix in targetmodelprefixes:
				
					for dspace_term in metadata:

						camelcase_class_name=make_camelcase_name(dspace_term)
						singular_fieldname=dspace_term.replace('.','_')
						plural_fieldname=singular_fieldname+'s'
						term_model_dict[dspace_term]={
							'classname':camelcase_class_name,
							'related_name':plural_fieldname
						}
						
# 						solrblock1="{\% %s \%}" %(dspace_term)
						solrblock="{%% for %s in object.%s.all %%}\n\t{{ %s.text_CN }}\n\t{{ %s.text_EN }}\n\t{{ %s.text_original}}\n{%% endfor %%}" %(singular_fieldname,plural_fieldname,singular_fieldname,singular_fieldname,singular_fieldname)
						solrblocks[targetmodelprefix].append(solrblock)
						admin_inline="class %s%sInLine(admin.TabularInline):\n\textra=0\n\tverbose_name_plural='%s'\n\tclasses=['collapse']\n\tmodel=%s%s.%s.through" %(targetmodelprefix,camelcase_class_name,dspace_term,targetmodelprefix,target_class_name,plural_fieldname)
						admin_inlines.append(admin_inline)
						target_admin_inlines_entries.append('%s%sInLine' %(targetmodelprefix,camelcase_class_name))
					
						admin_registrations.append("admin.site.register(%s)" %camelcase_class_name)

						serializer="class %sSerializer(serializers.ModelSerializer):\n\tclass Meta:\n\t\tmodel=%s\n\t\tfields='__all__'" %(camelcase_class_name,camelcase_class_name)
						serializers.append(serializer)
						nestedserializerline="%s=%sSerializer(many=True,read_only=True)" %(plural_fieldname,camelcase_class_name)
						nestedserializerlines.append(nestedserializerline)
				
						class_model="class %s(%s):\n\tclass Meta:\n\t\tverbose_name='%s'" %(camelcase_class_name,base_class_name,dspace_term)
						class_models.append(class_model)
				
						target_class_field="\t%s=models.ManyToManyField(%s)" %(plural_fieldname,camelcase_class_name)
						target_class_fields.append(target_class_field)
				
					#Serializers next

		admin_inlines=list(set(admin_inlines))
		class_models=list(set(class_models))
		target_class_fields=list(set(target_class_fields))
		target_admin_inlines_entries=list(set(target_admin_inlines_entries))
		admin_registrations=list(set(admin_registrations))

		print("------ADMIN INLINES\n","\n".join(admin_inlines))
		print("------ADMIN INLINE BLOCK---SPLIT!!!\n","(\n\t\t"+",\n\t\t".join(sorted(target_admin_inlines_entries))+'\n\t)')
		print("------ADMIN REGISTRATIONS BLOCK\n","\n".join(admin_registrations))
		
		print("------CLASS MODELS\n","\n".join(class_models))
		print("------TARGET CLASS FIELDS\n","\n".join(target_class_fields))
		
		print("-------SERIALIZERS","\n".join(serializers))
		
		serializerblock="from rest_framework import serializers\nfrom .models import *\nfrom metadata.models import *\n"

		serializerblock+="\n\n".join(serializers)+"\n\n"
		for targetmodelprefix in targetmodelprefixes:
			serializerblock += "class %s%sSerializer(serializers.ModelSerializer):\n\t" %(targetmodelprefix,target_class_name)
			serializerblock+="\n\t".join(nestedserializerlines)
			serializerblock+="\n\tclass Meta:\n\t\tmodel=%s%s\n\t\tfields='__all__'" %(targetmodelprefix,target_class_name)
			serializerblock+="\n\n"
		d=open('%s/serializers.py' %(target_app_name),'w')
		d.write(serializerblock)
		d.close()
		
		for targetmodelprefix in targetmodelprefixes:
			d=open("%s/templates/search/indexes/%s/%s%s_text.txt" %(target_app_name,target_app_name,targetmodelprefix.lower(),target_class_name.lower()),"w")
			d.write("\n".join(solrblocks[targetmodelprefix]))
			d.close()
			
		d=open('%s/dspace_term_model_map.py' %(target_app_name),'w')
		outstr="from %s.models import *\n" %(target_app_name)
		outstr+="\n\nterm_to_model={\n\t"
		dictliterallines=[]
		for term in term_model_dict:
			dictliterallines.append("'%s':%s" %(term,term_model_dict[term]))
		outstr+=",\n\t".join(dictliterallines)
		outstr+="\n}"
		d.write(outstr)
		d.close()
		
		
			
			
