from django.contrib import admin
from django import forms
from ads.models import *

class ProdTypeInLine(admin.TabularInline):
	extra=0
	model=Advertisement.prod_types.through

class ProdCatInline(admin.TabularInline):
	extra=0
	model=Advertisement.prod_cats.through

class GenreInLine(admin.TabularInline):
	extra=0
	model=Advertisement.genres.through
	
class SubjectInLine(admin.TabularInline):
	extra=0
	model=Advertisement.subjects.through

class LanguageInLine(admin.TabularInline):
	extra=0
	model=Language

class SpatialCoverageInLine(admin.TabularInline):
	extra=0
	model=Advertisement.spatial_coverage.through

# class TranscriptionAdmin(admin.ModelAdmin):
# 	model=Transcription

class TranscriptionInLine(admin.StackedInline):
	inlines=(
		LanguageInLine,
	)
	model=Transcription
	extra=0

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
		'subtitle_EN',
		'subtitle_CN',
		'dspace_uri',
		'dspace_iiif_uri',
		'uid',
		'pub_year',
		'owning_collection',
		'staged_photo',
		'is_current',
		'iiif_enabled',
		'description_fulltext'
	]
	list_display=('title','subtitle_EN','subtitle_CN','pub_year')
	search_fields=('title','pub_year','uid')
	model=Advertisement

class SubjectAdmin(admin.ModelAdmin):
	search_fields=('name_EN','name_CN')
	list_display=('name_EN','name_CN')

# Voyage (main section)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Collection)
admin.site.register(Language)
admin.site.register(Place)
admin.site.register(Subject,SubjectAdmin)