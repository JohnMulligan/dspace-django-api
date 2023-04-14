from django.db import models

# the standard field in the collection will have chinese & english text fields
# this will amount to a bilingual controlled vocabulary -- though I'm not certain that DSpace will allow us to "pair" these fields
class BilingualShortFieldAbstractBase(models.Model):
	text_original=models.CharField(max_length=500,null=True,blank=True)
	text_EN = models.CharField(max_length=500,null=True,blank=True)
	text_CN = models.CharField(max_length=500,null=True,blank=True)
	class Meta:
		unique_together=(['text_EN','text_CN'])
	def __str__(self):
		if self.text_EN is not None or self.text_CN is not None:
			label=" | ".join([i for i in [self.text_EN,self.text_CN] if i is not None])
		else:
			label=self.text_original
		return label
	class Meta:
		abstract = True

# for our transcription field (and maybe others but hopefully not too many) we'll have
# original text, english text, and chinese text
class BilingualTextFieldAbstractBase(models.Model):
	text_original = models.TextField(null=True,blank=True)
	text_EN = models.TextField(null=True,blank=True)
	text_CN = models.TextField(null=True,blank=True)
	def __str__(self):
		if self.text_EN is not None or self.text_CN is not None:
			label=" | ".join([i for i in [self.text_EN,self.text_CN] if i is not None])
		else:
			label=self.text_original
		label=label[:30]
		print(label)
		return label
	class Meta:
		abstract = True

class DcPublisher(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.publisher'
class DcCitationIssuenumber(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.citation.issueNumber'
class DcDescriptionProvenance(BilingualTextFieldAbstractBase):
	class Meta:
		verbose_name='dc.description.provenance'
class ChaoCompanyName(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='chao.company.name'
class DcDateCreated(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.date.created'
class DcDateAvailable(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.date.available'
class DcDateDigital(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.date.digital'
class DcRights(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.rights'
class DcCitationVolumenumber(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.citation.volumeNumber'
class DcDescriptionFulltext(BilingualTextFieldAbstractBase):
	class Meta:
		verbose_name='dc.description.fulltext'
class DcDateAccessioned(BilingualTextFieldAbstractBase):
	class Meta:
		verbose_name='dc.date.accessioned'
class DcSource(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.source'
class DcCitationPagenumber(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.citation.pageNumber'
class DcTypeGenre(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.type.genre'
class DcSourceCollection(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.source.collection'
class DcContributorPublisher(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.contributor.publisher'
class ChaoCompanyAddress(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='chao.company.address'
class ChaoProductagency(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='chao.productagency'
class ChaoContributorPrinter(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='chao.contributor.printer'
class ChaoDateChineselunar(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='chao.date.chineselunar'
class DcDateIssued(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.date.issued'
class DcIdentifierDigital(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.identifier.digital'
class DspaceIiifEnabled(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dspace.iiif.enabled'
class ChaoCompanyNation(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='chao.company.nation'
class DcSubjectProdtype(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.subject.prodtype'
class DcRightsUri(BilingualTextFieldAbstractBase):
	class Meta:
		verbose_name='dc.rights.uri'
class DcTitle(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.title'
class DcCoverageSpatial(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.coverage.spatial'
class DcSubjectProdcat(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.subject.prodcat'
class DcDescription(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.description'
class DcFormatMedium(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.format.medium'
class DcDescriptionPosition(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.description.position'
class DcSubjectAdcat(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.subject.adcat'
class DcSubjectBrand(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.subject.brand'
class DcRelationIspartofseries(BilingualTextFieldAbstractBase):
	class Meta:
		verbose_name='dc.relation.IsPartOfSeries'
class DcIdentifierUri(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.identifier.uri'
class DcTypeDcmi(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.type.dcmi'
class ChaoDateMinguo(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='chao.date.minguo'
class DcSubject(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.subject'
class DcContributorFunder(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.contributor.funder'
class DcLanguageIso(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='dc.language.iso'
class ChaoPrinterCheifeditor(BilingualShortFieldAbstractBase):
	class Meta:
		verbose_name='chao.printer.cheifeditor'
class DcDigitizationSpecifications(BilingualTextFieldAbstractBase):
	class Meta:
		verbose_name='dc.digitization.specifications'
class DcTitleSubtitle(BilingualTextFieldAbstractBase):
	class Meta:
		verbose_name='dc.title.subtitle'