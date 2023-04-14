from django.db import models
from metadata.models import *

# DSpace Collections
class Collection(models.Model):
	uid=models.CharField(max_length=50,null=False,blank=False,unique=True)
	name=models.CharField(max_length=50,null=False,blank=True)
	dspace_uri=models.URLField(max_length=250,null=False,blank=True)
	parent_collection=models.ForeignKey('self',null=True,on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class AdvertisementAbstractBase(models.Model):
	dc_contributor_funders=models.ManyToManyField(DcContributorFunder)
	dc_date_issueds=models.ManyToManyField(DcDateIssued)
	dc_identifier_uris=models.ManyToManyField(DcIdentifierUri)
	chao_date_chineselunars=models.ManyToManyField(ChaoDateChineselunar)
	dc_date_digitals=models.ManyToManyField(DcDateDigital)
	dc_date_availables=models.ManyToManyField(DcDateAvailable)
	dc_subject_prodcats=models.ManyToManyField(DcSubjectProdcat)
	dc_contributor_publishers=models.ManyToManyField(DcContributorPublisher)
	dc_type_dcmis=models.ManyToManyField(DcTypeDcmi)
	dspace_iiif_enableds=models.ManyToManyField(DspaceIiifEnabled)
	dc_description_provenances=models.ManyToManyField(DcDescriptionProvenance)
	chao_company_names=models.ManyToManyField(ChaoCompanyName)
	dc_sources=models.ManyToManyField(DcSource)
	chao_date_minguos=models.ManyToManyField(ChaoDateMinguo)
	chao_productagencys=models.ManyToManyField(ChaoProductagency)
	dc_subject_adcats=models.ManyToManyField(DcSubjectAdcat)
	chao_company_nations=models.ManyToManyField(ChaoCompanyNation)
	dc_digitization_specificationss=models.ManyToManyField(DcDigitizationSpecifications)
	dc_descriptions=models.ManyToManyField(DcDescription)
	dc_relation_IsPartOfSeriess=models.ManyToManyField(DcRelationIspartofseries)
	dc_citation_volumeNumbers=models.ManyToManyField(DcCitationVolumenumber)
	dc_description_positions=models.ManyToManyField(DcDescriptionPosition)
	dc_subjects=models.ManyToManyField(DcSubject)
	dc_language_isos=models.ManyToManyField(DcLanguageIso)
	dc_coverage_spatials=models.ManyToManyField(DcCoverageSpatial)
	dc_format_mediums=models.ManyToManyField(DcFormatMedium)
	dc_description_fulltexts=models.ManyToManyField(DcDescriptionFulltext)
	dc_citation_pageNumbers=models.ManyToManyField(DcCitationPagenumber)
	dc_rights_uris=models.ManyToManyField(DcRightsUri)
	dc_subject_brands=models.ManyToManyField(DcSubjectBrand)
	dc_subject_prodtypes=models.ManyToManyField(DcSubjectProdtype)
	dc_rightss=models.ManyToManyField(DcRights)
	dc_date_accessioneds=models.ManyToManyField(DcDateAccessioned)
	dc_source_collections=models.ManyToManyField(DcSourceCollection)
	dc_type_genres=models.ManyToManyField(DcTypeGenre)
	dc_title_subtitles=models.ManyToManyField(DcTitleSubtitle)
	dc_publishers=models.ManyToManyField(DcPublisher)
	dc_citation_issueNumbers=models.ManyToManyField(DcCitationIssuenumber)
	dc_titles=models.ManyToManyField(DcTitle)
	dc_date_createds=models.ManyToManyField(DcDateCreated)
	chao_printer_cheifeditors=models.ManyToManyField(ChaoPrinterCheifeditor)
	chao_company_addresss=models.ManyToManyField(ChaoCompanyAddress)
	dc_identifier_digitals=models.ManyToManyField(DcIdentifierDigital)
	chao_contributor_printers=models.ManyToManyField(ChaoContributorPrinter)
	pub_year=models.IntegerField(null=True,blank=True)
	owning_collection=models.ForeignKey(Collection,null=True,blank=True,on_delete=models.CASCADE)
	class Meta:
		abstract = True
	def __str__(self):
		label=self.dc_titles.first()
		if label is None:
			onestagedphoto=self.staged_photos.first()
			if onestagedphoto is not None:
				label=onestagedphoto.filename
			else:
				label=''
		else:
			label=label.__str__()
		return label
	class Meta:
		abstract = True

class PublishedAdvertisement(AdvertisementAbstractBase):
	uuid=models.CharField(max_length=50,null=False,blank=False,unique=True)
	dspace_uri=models.URLField(max_length=250,null=True,blank=True)
	dspace_iiif_uri=models.URLField(max_length=250,null=True,blank=True)
	iiif_enabled=models.BooleanField(default=False)
	is_current=models.BooleanField(default=False)

class StagedAdvertisement(AdvertisementAbstractBase):
	tmp_name=models.CharField(max_length=100,null=False,blank=False,unique=True)
	review_begun=models.BooleanField(default=False)
	review_finished=models.BooleanField(default=False)

class StagedPhoto(models.Model):
	filename=models.CharField(max_length=100,null=False,blank=False,unique=True)
	staged_photo=models.FileField(upload_to="staged_photos/",null=True,blank=True)
	parent_item=models.ForeignKey(StagedAdvertisement,null=False,blank=False,on_delete=models.CASCADE,related_name='staged_photos')
	def __str__(self):
		return self.filename