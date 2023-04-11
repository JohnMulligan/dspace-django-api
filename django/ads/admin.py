from django.contrib import admin
from django import forms
from ads.models import *

class ProdTypeInLine(admin.TabularInline):
# 	model=ProductType
	model=Advertisement.prod_types.through

class ProdCatInline(admin.TabularInline):
# 	model=ProductCategory
	model=Advertisement.prod_cats.through

class GenreInLine(admin.TabularInline):
# 	model=MediaType
	model=Advertisement.genres.through
	
class SubjectInLine(admin.TabularInline):
# 	model=Subject
	model=Advertisement.subjects.through

class SpatialCoverageInLine(admin.TabularInline):
# 	model=Place
	model=Advertisement.spatial_coverage.through

class TranscriptionInLine(admin.StackedInline):
	model=Advertisement.transcriptions.through

class AdvertisementAdmin(admin.ModelAdmin):
	inlines=(
		ProdTypeInLine,
		ProdCatInline,
		GenreInLine,
		SubjectInLine,
		SpatialCoverageInLine,
		TranscriptionInLine
	)
	fields=[
		'title',
		'dspace_uri',
		'dspace_iiif_uri',
		'uid',
		'pub_year',
		'owning_collection',
		'staged_photo'
	]
	list_display=('title','pub_year')
	search_fields=('title','pub_year')
	model=Advertisement

# Voyage (main section)
admin.site.register(Advertisement, AdvertisementAdmin)
