from django.contrib import admin
from django import forms
from ads.models import *

class ProdTypeInLine(admin.TabularInline):
	classes= ['collapse']
	extra=0
	model=Advertisement.prod_types.through

class ProdCatInline(admin.TabularInline):
	classes= ['collapse']
	extra=0
	model=Advertisement.prod_cats.through

class GenreInLine(admin.TabularInline):
	classes= ['collapse']
	extra=0
	model=Advertisement.genres.through
	
class SubjectInLine(admin.TabularInline):
	classes= ['collapse']
	extra=0
	model=Advertisement.subjects.through

class LanguageInLine(admin.TabularInline):
	classes= ['collapse']
	extra=0
	model=Language

class SpatialCoverageInLine(admin.TabularInline):
	classes= ['collapse']
	extra=0
	model=Advertisement.spatial_coverage.through

# class TranscriptionAdmin(admin.ModelAdmin):
# 	model=Transcription

class TranscriptionInLine(admin.StackedInline):
	inlines=(
		LanguageInLine,
	)
	model=Transcription
	classes= ['collapse']
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
admin.site.register(Language)