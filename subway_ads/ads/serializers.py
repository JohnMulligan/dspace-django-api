from rest_framework import serializers
from rest_framework.fields import SerializerMethodField,IntegerField,CharField
import re
from .models import *
import pprint
import gc
from tools.nest import nest_selected_fields

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
	def __init__(self, *args, **kwargs):
		dynamicfieldsserializermode=kwargs.pop('dynamicfieldsserializermode',None)
		selected_fields = kwargs.pop('selected_fields', None)
	
		super().__init__(*args, **kwargs)
		pp = pprint.PrettyPrinter(indent=4)
		if selected_fields is not None and dynamicfieldsserializermode:
			def nestthis(keychain,thisdict={}):
				while keychain:
					k=keychain.pop(0)
					kvs=k.split('__')
					if len(kvs)==2:
						i,v=kvs
						if i in thisdict:
							thisdict[i][v]={}
						else:
							thisdict[i]={v:{}}
				
					elif len(kvs)==1:
						thisdict[kvs[0]]={}
					else:
						i=kvs[0]
						j=['__'.join(kvs[1:])]
						if i in thisdict:
							thisdict[i]=nestthis(j,thisdict[i])
						else:
							thisdict[i]=nestthis(j,{})
				return thisdict
		
			selected_fields_dict=nestthis(selected_fields)
			print("--selected fields--")
			pp.pprint(selected_fields_dict)
			self=nest_selected_fields(self,selected_fields_dict)


class ProductTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=ProductType
		fields='__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=ProductCategory
		fields='__all__'
	
class MediaTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=MediaType
		fields='__all__'


class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=Subject
		fields='__all__'

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model=Place
		fields='__all__'

class CollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Collection
		fields='__all__'

class AdvertisementSerializer(DynamicFieldsModelSerializer):
	owning_collection=CollectionSerializer(many=False)
	spatial_coverage=PlaceSerializer(many=True,read_only=True)
	subject=SubjectSerializer(many=True,read_only=True)
	genre=MediaTypeSerializer(many=True,read_only=True)
	prod_cat=ProductCategorySerializer(many=True,read_only=True)
	prod_type=ProductTypeSerializer(many=True,read_only=True)
		
	class Meta:
		model=Advertisement
		fields='__all__'
		
		
