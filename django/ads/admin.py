from django.contrib import admin
from django import forms
from ads.models import *

class StagedDcIdentifierUriInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.identifier.uri'
	model=StagedAdvertisement.dc_identifier_uris.through
class PublishedDcCoverageSpatialInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.coverage.spatial'
	model=PublishedAdvertisement.dc_coverage_spatials.through
class PublishedDcDescriptionProvenanceInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.provenance'
	model=PublishedAdvertisement.dc_description_provenances.through
class PublishedDcLanguageIsoInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.language.iso'
	model=PublishedAdvertisement.dc_language_isos.through
class StagedDcSubjectBrandInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.brand'
	model=StagedAdvertisement.dc_subject_brands.through
class PublishedDcSubjectInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject'
	model=PublishedAdvertisement.dc_subjects.through
	extra=0
class PublishedDcDateCreatedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.created'
	model=PublishedAdvertisement.dc_date_createds.through
class PublishedDcSubjectProdcatInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.prodcat'
	model=PublishedAdvertisement.dc_subject_prodcats.through
class StagedDcLanguageIsoInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.language.iso'
	model=StagedAdvertisement.dc_language_isos.through
class PublishedDspaceIiifEnabledInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dspace.iiif.enabled'
	model=PublishedAdvertisement.dspace_iiif_enableds.through
class PublishedDcFormatMediumInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.format.medium'
	model=PublishedAdvertisement.dc_format_mediums.through
class PublishedDcTitleInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.title'
	model=PublishedAdvertisement.dc_titles.through
class StagedDcTypeGenreInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.type.genre'
	model=StagedAdvertisement.dc_type_genres.through
class StagedDcSubjectProdcatInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.prodcat'
	model=StagedAdvertisement.dc_subject_prodcats.through
	extra=0
class StagedDcCoverageSpatialInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.coverage.spatial'
	model=StagedAdvertisement.dc_coverage_spatials.through
class StagedDcPublisherInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.publisher'
	model=StagedAdvertisement.dc_publishers.through
class PublishedDcTypeDcmiInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.type.dcmi'
	model=PublishedAdvertisement.dc_type_dcmis.through
	extra=0
class StagedDcSubjectProdtypeInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.prodtype'
	model=StagedAdvertisement.dc_subject_prodtypes.through
class StagedDcDateIssuedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.issued'
	model=StagedAdvertisement.dc_date_issueds.through
class PublishedDcDateIssuedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.issued'
	model=PublishedAdvertisement.dc_date_issueds.through
class PublishedDcSubjectBrandInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.brand'
	model=PublishedAdvertisement.dc_subject_brands.through
class PublishedDcTitleSubtitleInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.title.subtitle'
	model=PublishedAdvertisement.dc_title_subtitles.through
class PublishedDcDescriptionFulltextInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.fulltext'
	model=PublishedAdvertisement.dc_description_fulltexts.through
class PublishedDcPublisherInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.publisher'
	model=PublishedAdvertisement.dc_publishers.through
class StagedDcDateAvailableInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.available'
	model=StagedAdvertisement.dc_date_availables.through
class StagedDcDescriptionProvenanceInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.provenance'
	model=StagedAdvertisement.dc_description_provenances.through
class PublishedDcSourceCollectionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.source.collection'
class StagedDcDescriptionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description'
	model=StagedAdvertisement.dc_descriptions.through
class StagedDcTypeDcmiInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.type.dcmi'
	model=StagedAdvertisement.dc_type_dcmis.through
class PublishedDcIdentifierUriInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.identifier.uri'
	model=PublishedAdvertisement.dc_identifier_uris.through
class PublishedDcSubjectProdtypeInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.prodtype'
	model=PublishedAdvertisement.dc_subject_prodtypes.through
class PublishedDcTypeGenreInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.type.genre'
	model=PublishedAdvertisement.dc_type_genres.through
class StagedDcDateCreatedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.created'
	model=StagedAdvertisement.dc_date_createds.through
class PublishedDcDateAvailableInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.available'
	model=PublishedAdvertisement.dc_date_availables.through
class PublishedDcDescriptionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description'
	model=PublishedAdvertisement.dc_descriptions.through
class StagedDcSourceCollectionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.source.collection'
	model=StagedAdvertisement.dc_source_collections.through
class StagedDcSubjectInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject'
	model=StagedAdvertisement.dc_subjects.through
class PublishedDcDigitizationSpecificationsInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.digitization.specifications'
	model=PublishedAdvertisement.dc_digitization_specificationss.through
class StagedDcDigitizationSpecificationsInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.digitization.specifications'
	model=StagedAdvertisement.dc_digitization_specificationss.through
class StagedDcDescriptionFulltextInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.fulltext'
	model=StagedAdvertisement.dc_description_fulltexts.through
class StagedDcFormatMediumInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.format.medium'
	model=StagedAdvertisement.dc_format_mediums.through
class StagedDcDateAccessionedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.accessioned'
	model=StagedAdvertisement.dc_date_accessioneds.through
	extra=0
class StagedDcTitleInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.title'
	model=StagedAdvertisement.dc_titles.through
class StagedDcIdentifierDigitalInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.identifier.digital'
	model=StagedAdvertisement.dc_identifier_digitals.through
	extra=0
class PublishedDcIdentifierDigitalInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.identifier.digital'
	model=PublishedAdvertisement.dc_identifier_digitals.through
class StagedDspaceIiifEnabledInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dspace.iiif.enabled'
	model=StagedAdvertisement.dspace_iiif_enableds.through
class PublishedDcDateAccessionedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.accessioned'
	model=PublishedAdvertisement.dc_date_accessioneds.through
class StagedDcTitleSubtitleInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.title.subtitle'
	model=StagedAdvertisement.dc_title_subtitles.through

	
class PublishedAdvertisementAdmin(admin.ModelAdmin):
	inlines=(
		PublishedDcCoverageSpatialInLine,
		PublishedDcDateAccessionedInLine,
		PublishedDcDateAvailableInLine,
		PublishedDcDateCreatedInLine,
		PublishedDcDateIssuedInLine,
		PublishedDcDescriptionFulltextInLine,
		PublishedDcDescriptionInLine,
		PublishedDcDescriptionProvenanceInLine,
		PublishedDcDigitizationSpecificationsInLine,
		PublishedDcFormatMediumInLine,
		PublishedDcIdentifierDigitalInLine,
		PublishedDcIdentifierUriInLine,
		PublishedDcLanguageIsoInLine,
		PublishedDcPublisherInLine,
		PublishedDcSubjectBrandInLine,
		PublishedDcSubjectInLine,
		PublishedDcSubjectProdcatInLine,
		PublishedDcSubjectProdtypeInLine,
		PublishedDcTitleInLine,
		PublishedDcTitleSubtitleInLine,
		PublishedDcTypeDcmiInLine,
		PublishedDcTypeGenreInLine,
		PublishedDspaceIiifEnabledInLine
	)

	fields=[
		'dspace_uri',
		'dspace_iiif_uri',
		'uuid',
		'pub_year',
		'owning_collection',
		'iiif_enabled',
		'is_current'
	]

	@admin.display(ordering='dc_titles__text_original', description='Title')
	def get_titles(self, obj):
		return obj.dc_titles.first()
	
	list_display=('get_titles','owning_collection','uuid')
	search_fields=('get_titles','owning_collection','uuid')







class StagedPhotoInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='staged photos'
	model=StagedPhoto

class StagedAdvertisementAdmin(admin.ModelAdmin):
	inlines=(
		StagedPhotoInLine,
		StagedDcDescriptionFulltextInLine,
		StagedDcCoverageSpatialInLine,
		StagedDcDateAccessionedInLine,
		StagedDcDateAvailableInLine,
		StagedDcDateCreatedInLine,
		StagedDcDateIssuedInLine,
		StagedDcDescriptionInLine,
		StagedDcDescriptionProvenanceInLine,
		StagedDcDigitizationSpecificationsInLine,
		StagedDcFormatMediumInLine,
		StagedDcIdentifierDigitalInLine,
		StagedDcIdentifierUriInLine,
		StagedDcLanguageIsoInLine,
		StagedDcPublisherInLine,
		StagedDcSourceCollectionInLine,
		StagedDcSubjectBrandInLine,
		StagedDcSubjectInLine,
		StagedDcSubjectProdcatInLine,
		StagedDcSubjectProdtypeInLine,
		StagedDcTitleInLine,
		StagedDcTitleSubtitleInLine,
		StagedDcTypeDcmiInLine,
		StagedDcTypeGenreInLine,
		StagedDspaceIiifEnabledInLine
	)

	fields=[
		'tmp_name',
		'pub_year',
		'review_begun',
		'review_finished'
	]

	@admin.display(ordering='dc_titles__text_original', description='Title')
	def get_titles(self, obj):
		if obj.dc_titles.first() is None:
			label=''
		else:
			obj.dc_titles.first().__str__
		return label
	
	list_display=('tmp_name','get_titles','owning_collection','review_begun','review_finished')
	search_fields=('get_titles','owning_collection')

class StagedPhotoAdmin(admin.ModelAdmin):
	
	@admin.display(ordering='parent_item.tmp_name', description='Parent Temp Title')
	def parent_name(self, obj):
		return obj.parent_item.tmp_name
	
	list_display=('filename','parent_name')


admin.site.register(PublishedAdvertisement, PublishedAdvertisementAdmin)
admin.site.register(StagedAdvertisement, StagedAdvertisementAdmin)
admin.site.register(Collection)
admin.site.register(StagedPhoto,StagedPhotoAdmin)