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
	dc_date_issueds=models.ManyToManyField(DcDateIssued)
	dc_identifier_uris=models.ManyToManyField(DcIdentifierUri)
	dc_date_availables=models.ManyToManyField(DcDateAvailable)
	dc_subject_prodcats=models.ManyToManyField(DcSubjectProdcat)
	dc_type_dcmis=models.ManyToManyField(DcTypeDcmi)
	dspace_iiif_enableds=models.ManyToManyField(DspaceIiifEnabled)
	dc_description_provenances=models.ManyToManyField(DcDescriptionProvenance)
	dc_digitization_specificationss=models.ManyToManyField(DcDigitizationSpecifications)
	dc_descriptions=models.ManyToManyField(DcDescription)
	dc_subjects=models.ManyToManyField(DcSubject)
	dc_language_isos=models.ManyToManyField(DcLanguageIso)
	dc_coverage_spatials=models.ManyToManyField(DcCoverageSpatial)
	dc_format_mediums=models.ManyToManyField(DcFormatMedium)
	dc_description_fulltexts=models.ManyToManyField(DcDescriptionFulltext)
	dc_subject_brands=models.ManyToManyField(DcSubjectBrand)
	dc_subject_prodtypes=models.ManyToManyField(DcSubjectProdtype)
	dc_date_accessioneds=models.ManyToManyField(DcDateAccessioned)
	dc_source_collections=models.ManyToManyField(DcSourceCollection)
	dc_type_genres=models.ManyToManyField(DcTypeGenre)
	dc_title_subtitles=models.ManyToManyField(DcTitleSubtitle)
	dc_publishers=models.ManyToManyField(DcPublisher)
	dc_titles=models.ManyToManyField(DcTitle)
	dc_date_createds=models.ManyToManyField(DcDateCreated)
	dc_identifier_digitals=models.ManyToManyField(DcIdentifierDigital)
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