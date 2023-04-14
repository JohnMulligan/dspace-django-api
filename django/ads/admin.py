from django.contrib import admin
from django import forms
from ads.models import *

class StagedDcIdentifierUriInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.identifier.uri'
	classes=['collapse']
	model=StagedAdvertisement.dc_identifier_uris.through
class PublishedDcCoverageSpatialInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.coverage.spatial'
	classes=['collapse']
	model=PublishedAdvertisement.dc_coverage_spatials.through
class StagedDcSourceInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.source'
	classes=['collapse']
	model=StagedAdvertisement.dc_sources.through
class StagedDcCitationVolumenumberInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.citation.volumeNumber'
	classes=['collapse']
	model=StagedAdvertisement.dc_citation_volumeNumbers.through
class PublishedDcDescriptionProvenanceInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.provenance'
	classes=['collapse']
	model=PublishedAdvertisement.dc_description_provenances.through
class PublishedDcLanguageIsoInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.language.iso'
	classes=['collapse']
	model=PublishedAdvertisement.dc_language_isos.through
class StagedDcSubjectBrandInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.brand'
	classes=['collapse']
	model=StagedAdvertisement.dc_subject_brands.through
class PublishedDcSubjectInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject'
	classes=['collapse']
	model=PublishedAdvertisement.dc_subjects.through
class PublishedDcDateDigitalInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.digital'
	classes=['collapse']
	model=PublishedAdvertisement.dc_date_digitals.through
	extra=0
	classes=['collapse']
class StagedDcRelationIspartofseriesInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.relation.IsPartOfSeries'
	classes=['collapse']
	model=StagedAdvertisement.dc_relation_IsPartOfSeriess.through
class PublishedDcDateCreatedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.created'
	classes=['collapse']
	model=PublishedAdvertisement.dc_date_createds.through
	extra=0
	classes=['collapse']
class PublishedDcSubjectProdcatInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.prodcat'
	classes=['collapse']
	model=PublishedAdvertisement.dc_subject_prodcats.through
	extra=0
	classes=['collapse']
class StagedDcLanguageIsoInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.language.iso'
	classes=['collapse']
	model=StagedAdvertisement.dc_language_isos.through
class PublishedDcSourceInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.source'
	classes=['collapse']
	model=PublishedAdvertisement.dc_sources.through
class PublishedDcDescriptionPositionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.position'
	classes=['collapse']
	model=PublishedAdvertisement.dc_description_positions.through
class StagedDcDateDigitalInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.digital'
	classes=['collapse']
	model=StagedAdvertisement.dc_date_digitals.through
	extra=0
	classes=['collapse']
class PublishedDspaceIiifEnabledInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dspace.iiif.enabled'
	classes=['collapse']
	model=PublishedAdvertisement.dspace_iiif_enableds.through
class PublishedDcContributorPublisherInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.contributor.publisher'
	classes=['collapse']
	model=PublishedAdvertisement.dc_contributor_publishers.through
class PublishedDcFormatMediumInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.format.medium'
	classes=['collapse']
	model=PublishedAdvertisement.dc_format_mediums.through
class PublishedDcTitleInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.title'
	classes=['collapse']
	model=PublishedAdvertisement.dc_titles.through
class StagedDcTypeGenreInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.type.genre'
	classes=['collapse']
	model=StagedAdvertisement.dc_type_genres.through
class StagedDcSubjectProdcatInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.prodcat'
	classes=['collapse']
	model=StagedAdvertisement.dc_subject_prodcats.through
	extra=0
	classes=['collapse']
class StagedDcCoverageSpatialInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.coverage.spatial'
	classes=['collapse']
	model=StagedAdvertisement.dc_coverage_spatials.through
class StagedDcRightsUriInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.rights.uri'
	classes=['collapse']
	model=StagedAdvertisement.dc_rights_uris.through
class StagedDcPublisherInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.publisher'
	classes=['collapse']
	model=StagedAdvertisement.dc_publishers.through
class PublishedDcTypeDcmiInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.type.dcmi'
	classes=['collapse']
	model=PublishedAdvertisement.dc_type_dcmis.through
	extra=0
	classes=['collapse']
class StagedDcSubjectProdtypeInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.prodtype'
	classes=['collapse']
	model=StagedAdvertisement.dc_subject_prodtypes.through
class PublishedDcCitationPagenumberInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.citation.pageNumber'
	classes=['collapse']
	model=PublishedAdvertisement.dc_citation_pageNumbers.through
class StagedDcDateIssuedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.issued'
	classes=['collapse']
	model=StagedAdvertisement.dc_date_issueds.through
class PublishedDcDateIssuedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.issued'
	classes=['collapse']
	model=PublishedAdvertisement.dc_date_issueds.through
class PublishedDcRelationIspartofseriesInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.relation.IsPartOfSeries'
	classes=['collapse']
	model=PublishedAdvertisement.dc_relation_IsPartOfSeriess.through
	extra=0
	classes=['collapse']
	extra=0
	classes=['collapse']
class PublishedDcSubjectBrandInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.brand'
	classes=['collapse']
	model=PublishedAdvertisement.dc_subject_brands.through
class PublishedDcTitleSubtitleInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.title.subtitle'
	classes=['collapse']
	model=PublishedAdvertisement.dc_title_subtitles.through
class PublishedDcDescriptionFulltextInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.fulltext'
	classes=['collapse']
	model=PublishedAdvertisement.dc_description_fulltexts.through
class PublishedDcPublisherInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.publisher'
	classes=['collapse']
	model=PublishedAdvertisement.dc_publishers.through
class StagedDcRightsInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.rights'
	classes=['collapse']
	model=StagedAdvertisement.dc_rightss.through
class StagedDcDateAvailableInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.available'
	classes=['collapse']
	model=StagedAdvertisement.dc_date_availables.through
class StagedDcContributorFunderInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.contributor.funder'
	classes=['collapse']
	model=StagedAdvertisement.dc_contributor_funders.through
class StagedDcSubjectAdcatInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.adcat'
	classes=['collapse']
	model=StagedAdvertisement.dc_subject_adcats.through
class StagedDcDescriptionProvenanceInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.provenance'
	classes=['collapse']
	model=StagedAdvertisement.dc_description_provenances.through
	extra=0
	classes=['collapse']
class PublishedDcRightsUriInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.rights.uri'
	classes=['collapse']
	model=PublishedAdvertisement.dc_rights_uris.through
	extra=0
	classes=['collapse']
	extra=0
	classes=['collapse']
class PublishedDcSourceCollectionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.source.collection'
	classes=['collapse']
	model=PublishedAdvertisement.dc_source_collections.through
class StagedDcCitationIssuenumberInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.citation.issueNumber'
	classes=['collapse']
	model=StagedAdvertisement.dc_citation_issueNumbers.through
class PublishedDcSubjectAdcatInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.adcat'
	classes=['collapse']
	model=PublishedAdvertisement.dc_subject_adcats.through
class StagedDcDescriptionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description'
	classes=['collapse']
	model=StagedAdvertisement.dc_descriptions.through
class StagedDcTypeDcmiInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.type.dcmi'
	classes=['collapse']
	model=StagedAdvertisement.dc_type_dcmis.through
class PublishedDcIdentifierUriInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.identifier.uri'
	classes=['collapse']
	model=PublishedAdvertisement.dc_identifier_uris.through
class PublishedDcSubjectProdtypeInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject.prodtype'
	classes=['collapse']
	model=PublishedAdvertisement.dc_subject_prodtypes.through
class PublishedDcTypeGenreInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.type.genre'
	classes=['collapse']
	model=PublishedAdvertisement.dc_type_genres.through
class StagedDcCitationPagenumberInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.citation.pageNumber'
	classes=['collapse']
	model=StagedAdvertisement.dc_citation_pageNumbers.through
class StagedDcDateCreatedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.created'
	classes=['collapse']
	model=StagedAdvertisement.dc_date_createds.through
class PublishedDcCitationVolumenumberInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.citation.volumeNumber'
	classes=['collapse']
	model=PublishedAdvertisement.dc_citation_volumeNumbers.through
class PublishedDcDateAvailableInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.available'
	classes=['collapse']
	model=PublishedAdvertisement.dc_date_availables.through
class PublishedDcDescriptionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description'
	classes=['collapse']
	model=PublishedAdvertisement.dc_descriptions.through
class StagedDcSourceCollectionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.source.collection'
	classes=['collapse']
	model=StagedAdvertisement.dc_source_collections.through
class StagedDcSubjectInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.subject'
	classes=['collapse']
	model=StagedAdvertisement.dc_subjects.through
class PublishedDcDigitizationSpecificationsInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.digitization.specifications'
	classes=['collapse']
	model=PublishedAdvertisement.dc_digitization_specificationss.through
class StagedDcContributorPublisherInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.contributor.publisher'
	classes=['collapse']
	model=StagedAdvertisement.dc_contributor_publishers.through
class StagedDcDigitizationSpecificationsInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.digitization.specifications'
	classes=['collapse']
	model=StagedAdvertisement.dc_digitization_specificationss.through
class StagedDcDescriptionFulltextInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.fulltext'
	model=StagedAdvertisement.dc_description_fulltexts.through
class StagedDcFormatMediumInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.format.medium'
	classes=['collapse']
	model=StagedAdvertisement.dc_format_mediums.through
class StagedDcDateAccessionedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.accessioned'
	classes=['collapse']
	model=StagedAdvertisement.dc_date_accessioneds.through
	extra=0
	classes=['collapse']
class StagedDcTitleInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.title'
	classes=['collapse']
	model=StagedAdvertisement.dc_titles.through
	extra=0
	classes=['collapse']
	extra=0
	classes=['collapse']
class PublishedDcCitationIssuenumberInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.citation.issueNumber'
	classes=['collapse']
	model=PublishedAdvertisement.dc_citation_issueNumbers.through
	extra=0
	classes=['collapse']
class StagedDcDescriptionPositionInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.description.position'
	classes=['collapse']
	model=StagedAdvertisement.dc_description_positions.through
class StagedDcIdentifierDigitalInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.identifier.digital'
	classes=['collapse']
	model=StagedAdvertisement.dc_identifier_digitals.through
	extra=0
	classes=['collapse']
class PublishedDcIdentifierDigitalInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.identifier.digital'
	classes=['collapse']
	model=PublishedAdvertisement.dc_identifier_digitals.through
class StagedDspaceIiifEnabledInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dspace.iiif.enabled'
	classes=['collapse']
	model=StagedAdvertisement.dspace_iiif_enableds.through
class PublishedDcContributorFunderInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.contributor.funder'
	classes=['collapse']
	model=PublishedAdvertisement.dc_contributor_funders.through
class PublishedDcDateAccessionedInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.date.accessioned'
	classes=['collapse']
	model=PublishedAdvertisement.dc_date_accessioneds.through
class PublishedDcRightsInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.rights'
	classes=['collapse']
	model=PublishedAdvertisement.dc_rightss.through
class StagedDcTitleSubtitleInLine(admin.TabularInline):
	extra=0
	verbose_name_plural='dc.title.subtitle'
	classes=['collapse']
	model=StagedAdvertisement.dc_title_subtitles.through

	
class PublishedAdvertisementAdmin(admin.ModelAdmin):
	inlines=(
		PublishedDcCitationIssuenumberInLine,
		PublishedDcCitationPagenumberInLine,
		PublishedDcCitationVolumenumberInLine,
		PublishedDcContributorFunderInLine,
		PublishedDcContributorPublisherInLine,
		PublishedDcCoverageSpatialInLine,
		PublishedDcDateAccessionedInLine,
		PublishedDcDateAvailableInLine,
		PublishedDcDateCreatedInLine,
		PublishedDcDateDigitalInLine,
		PublishedDcDateIssuedInLine,
		PublishedDcDescriptionFulltextInLine,
		PublishedDcDescriptionInLine,
		PublishedDcDescriptionPositionInLine,
		PublishedDcDescriptionProvenanceInLine,
		PublishedDcDigitizationSpecificationsInLine,
		PublishedDcFormatMediumInLine,
		PublishedDcIdentifierDigitalInLine,
		PublishedDcIdentifierUriInLine,
		PublishedDcLanguageIsoInLine,
		PublishedDcPublisherInLine,
		PublishedDcRelationIspartofseriesInLine,
		PublishedDcRightsInLine,
		PublishedDcRightsUriInLine,
		PublishedDcSourceCollectionInLine,
		PublishedDcSourceInLine,
		PublishedDcSubjectAdcatInLine,
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
		StagedDcCitationIssuenumberInLine,
		StagedDcCitationPagenumberInLine,
		StagedDcCitationVolumenumberInLine,
		StagedDcContributorFunderInLine,
		StagedDcContributorPublisherInLine,
		StagedDcCoverageSpatialInLine,
		StagedDcDateAccessionedInLine,
		StagedDcDateAvailableInLine,
		StagedDcDateCreatedInLine,
		StagedDcDateDigitalInLine,
		StagedDcDateIssuedInLine,
		StagedDcDescriptionInLine,
		StagedDcDescriptionPositionInLine,
		StagedDcDescriptionProvenanceInLine,
		StagedDcDigitizationSpecificationsInLine,
		StagedDcFormatMediumInLine,
		StagedDcIdentifierDigitalInLine,
		StagedDcIdentifierUriInLine,
		StagedDcLanguageIsoInLine,
		StagedDcPublisherInLine,
		StagedDcRelationIspartofseriesInLine,
		StagedDcRightsInLine,
		StagedDcRightsUriInLine,
		StagedDcSourceCollectionInLine,
		StagedDcSourceInLine,
		StagedDcSubjectAdcatInLine,
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