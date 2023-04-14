from rest_framework import serializers
from .models import *
from metadata.models import *
class ChaoCompanyAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyAddress
		fields='__all__'

class ChaoCompanyNameSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyName
		fields='__all__'

class ChaoCompanyNationSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyNation
		fields='__all__'

class ChaoContributorPrinterSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoContributorPrinter
		fields='__all__'

class ChaoDateChineselunarSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoDateChineselunar
		fields='__all__'

class ChaoDateMinguoSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoDateMinguo
		fields='__all__'

class ChaoPrinterCheifeditorSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoPrinterCheifeditor
		fields='__all__'

class ChaoProductagencySerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoProductagency
		fields='__all__'

class DcCitationPagenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationPagenumber
		fields='__all__'

class DcCitationVolumenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationVolumenumber
		fields='__all__'

class DcContributorFunderSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcContributorFunder
		fields='__all__'

class DcContributorPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcContributorPublisher
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateDigital
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionFulltextSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionFulltext
		fields='__all__'

class DcDescriptionPositionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionPosition
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcRelationIspartofseriesSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRelationIspartofseries
		fields='__all__'

class DcRightsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRights
		fields='__all__'

class DcRightsUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRightsUri
		fields='__all__'

class DcSourceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSource
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectAdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectAdcat
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class ChaoCompanyAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyAddress
		fields='__all__'

class ChaoCompanyNameSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyName
		fields='__all__'

class ChaoCompanyNationSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyNation
		fields='__all__'

class ChaoContributorPrinterSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoContributorPrinter
		fields='__all__'

class ChaoDateChineselunarSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoDateChineselunar
		fields='__all__'

class ChaoDateMinguoSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoDateMinguo
		fields='__all__'

class ChaoPrinterCheifeditorSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoPrinterCheifeditor
		fields='__all__'

class ChaoProductagencySerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoProductagency
		fields='__all__'

class DcCitationPagenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationPagenumber
		fields='__all__'

class DcCitationVolumenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationVolumenumber
		fields='__all__'

class DcContributorFunderSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcContributorFunder
		fields='__all__'

class DcContributorPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcContributorPublisher
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateDigital
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionFulltextSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionFulltext
		fields='__all__'

class DcDescriptionPositionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionPosition
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcRelationIspartofseriesSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRelationIspartofseries
		fields='__all__'

class DcRightsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRights
		fields='__all__'

class DcRightsUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRightsUri
		fields='__all__'

class DcSourceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSource
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectAdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectAdcat
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class ChaoCompanyAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyAddress
		fields='__all__'

class ChaoCompanyNameSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyName
		fields='__all__'

class ChaoCompanyNationSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyNation
		fields='__all__'

class ChaoContributorPrinterSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoContributorPrinter
		fields='__all__'

class ChaoDateMinguoSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoDateMinguo
		fields='__all__'

class ChaoPrinterCheifeditorSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoPrinterCheifeditor
		fields='__all__'

class ChaoProductagencySerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoProductagency
		fields='__all__'

class DcCitationIssuenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationIssuenumber
		fields='__all__'

class DcCitationPagenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationPagenumber
		fields='__all__'

class DcCitationVolumenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationVolumenumber
		fields='__all__'

class DcContributorFunderSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcContributorFunder
		fields='__all__'

class DcContributorPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcContributorPublisher
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateDigital
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionFulltextSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionFulltext
		fields='__all__'

class DcDescriptionPositionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionPosition
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcRelationIspartofseriesSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRelationIspartofseries
		fields='__all__'

class DcRightsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRights
		fields='__all__'

class DcRightsUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRightsUri
		fields='__all__'

class DcSourceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSource
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectAdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectAdcat
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DspaceIiifEnabledSerializer(serializers.ModelSerializer):
	class Meta:
		model=DspaceIiifEnabled
		fields='__all__'

class ChaoCompanyAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyAddress
		fields='__all__'

class ChaoCompanyNameSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyName
		fields='__all__'

class ChaoCompanyNationSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoCompanyNation
		fields='__all__'

class ChaoContributorPrinterSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoContributorPrinter
		fields='__all__'

class ChaoDateMinguoSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoDateMinguo
		fields='__all__'

class ChaoPrinterCheifeditorSerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoPrinterCheifeditor
		fields='__all__'

class ChaoProductagencySerializer(serializers.ModelSerializer):
	class Meta:
		model=ChaoProductagency
		fields='__all__'

class DcCitationIssuenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationIssuenumber
		fields='__all__'

class DcCitationPagenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationPagenumber
		fields='__all__'

class DcCitationVolumenumberSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCitationVolumenumber
		fields='__all__'

class DcContributorFunderSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcContributorFunder
		fields='__all__'

class DcContributorPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcContributorPublisher
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateDigital
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionFulltextSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionFulltext
		fields='__all__'

class DcDescriptionPositionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionPosition
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcRelationIspartofseriesSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRelationIspartofseries
		fields='__all__'

class DcRightsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRights
		fields='__all__'

class DcRightsUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcRightsUri
		fields='__all__'

class DcSourceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSource
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectAdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectAdcat
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DspaceIiifEnabledSerializer(serializers.ModelSerializer):
	class Meta:
		model=DspaceIiifEnabled
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DspaceIiifEnabledSerializer(serializers.ModelSerializer):
	class Meta:
		model=DspaceIiifEnabled
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DspaceIiifEnabledSerializer(serializers.ModelSerializer):
	class Meta:
		model=DspaceIiifEnabled
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class DcCoverageSpatialSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcCoverageSpatial
		fields='__all__'

class DcDateAccessionedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAccessioned
		fields='__all__'

class DcDateAvailableSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateAvailable
		fields='__all__'

class DcDateCreatedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateCreated
		fields='__all__'

class DcDateIssuedSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDateIssued
		fields='__all__'

class DcDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescription
		fields='__all__'

class DcDescriptionProvenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDescriptionProvenance
		fields='__all__'

class DcDigitizationSpecificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcDigitizationSpecifications
		fields='__all__'

class DcFormatMediumSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcFormatMedium
		fields='__all__'

class DcIdentifierDigitalSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierDigital
		fields='__all__'

class DcIdentifierUriSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcIdentifierUri
		fields='__all__'

class DcLanguageIsoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcLanguageIso
		fields='__all__'

class DcPublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcPublisher
		fields='__all__'

class DcSourceCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSourceCollection
		fields='__all__'

class DcSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubject
		fields='__all__'

class DcSubjectBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectBrand
		fields='__all__'

class DcSubjectProdcatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdcat
		fields='__all__'

class DcSubjectProdtypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcSubjectProdtype
		fields='__all__'

class DcTitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitle
		fields='__all__'

class DcTitleSubtitleSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTitleSubtitle
		fields='__all__'

class DcTypeDcmiSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeDcmi
		fields='__all__'

class DcTypeGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model=DcTypeGenre
		fields='__all__'

class PublishedAdvertisementSerializer(serializers.ModelSerializer):
	chao_company_addresss=ChaoCompanyAddressSerializer(many=True,read_only=True)
	chao_company_names=ChaoCompanyNameSerializer(many=True,read_only=True)
	chao_company_nations=ChaoCompanyNationSerializer(many=True,read_only=True)
	chao_contributor_printers=ChaoContributorPrinterSerializer(many=True,read_only=True)
	chao_date_chineselunars=ChaoDateChineselunarSerializer(many=True,read_only=True)
	chao_date_minguos=ChaoDateMinguoSerializer(many=True,read_only=True)
	chao_printer_cheifeditors=ChaoPrinterCheifeditorSerializer(many=True,read_only=True)
	chao_productagencys=ChaoProductagencySerializer(many=True,read_only=True)
	dc_citation_pageNumbers=DcCitationPagenumberSerializer(many=True,read_only=True)
	dc_citation_volumeNumbers=DcCitationVolumenumberSerializer(many=True,read_only=True)
	dc_contributor_funders=DcContributorFunderSerializer(many=True,read_only=True)
	dc_contributor_publishers=DcContributorPublisherSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_digitals=DcDateDigitalSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_fulltexts=DcDescriptionFulltextSerializer(many=True,read_only=True)
	dc_description_positions=DcDescriptionPositionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_relation_IsPartOfSeriess=DcRelationIspartofseriesSerializer(many=True,read_only=True)
	dc_rightss=DcRightsSerializer(many=True,read_only=True)
	dc_rights_uris=DcRightsUriSerializer(many=True,read_only=True)
	dc_sources=DcSourceSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_adcats=DcSubjectAdcatSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	chao_company_addresss=ChaoCompanyAddressSerializer(many=True,read_only=True)
	chao_company_names=ChaoCompanyNameSerializer(many=True,read_only=True)
	chao_company_nations=ChaoCompanyNationSerializer(many=True,read_only=True)
	chao_contributor_printers=ChaoContributorPrinterSerializer(many=True,read_only=True)
	chao_date_chineselunars=ChaoDateChineselunarSerializer(many=True,read_only=True)
	chao_date_minguos=ChaoDateMinguoSerializer(many=True,read_only=True)
	chao_printer_cheifeditors=ChaoPrinterCheifeditorSerializer(many=True,read_only=True)
	chao_productagencys=ChaoProductagencySerializer(many=True,read_only=True)
	dc_citation_pageNumbers=DcCitationPagenumberSerializer(many=True,read_only=True)
	dc_citation_volumeNumbers=DcCitationVolumenumberSerializer(many=True,read_only=True)
	dc_contributor_funders=DcContributorFunderSerializer(many=True,read_only=True)
	dc_contributor_publishers=DcContributorPublisherSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_digitals=DcDateDigitalSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_fulltexts=DcDescriptionFulltextSerializer(many=True,read_only=True)
	dc_description_positions=DcDescriptionPositionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_relation_IsPartOfSeriess=DcRelationIspartofseriesSerializer(many=True,read_only=True)
	dc_rightss=DcRightsSerializer(many=True,read_only=True)
	dc_rights_uris=DcRightsUriSerializer(many=True,read_only=True)
	dc_sources=DcSourceSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_adcats=DcSubjectAdcatSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	chao_company_addresss=ChaoCompanyAddressSerializer(many=True,read_only=True)
	chao_company_names=ChaoCompanyNameSerializer(many=True,read_only=True)
	chao_company_nations=ChaoCompanyNationSerializer(many=True,read_only=True)
	chao_contributor_printers=ChaoContributorPrinterSerializer(many=True,read_only=True)
	chao_date_minguos=ChaoDateMinguoSerializer(many=True,read_only=True)
	chao_printer_cheifeditors=ChaoPrinterCheifeditorSerializer(many=True,read_only=True)
	chao_productagencys=ChaoProductagencySerializer(many=True,read_only=True)
	dc_citation_issueNumbers=DcCitationIssuenumberSerializer(many=True,read_only=True)
	dc_citation_pageNumbers=DcCitationPagenumberSerializer(many=True,read_only=True)
	dc_citation_volumeNumbers=DcCitationVolumenumberSerializer(many=True,read_only=True)
	dc_contributor_funders=DcContributorFunderSerializer(many=True,read_only=True)
	dc_contributor_publishers=DcContributorPublisherSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_digitals=DcDateDigitalSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_fulltexts=DcDescriptionFulltextSerializer(many=True,read_only=True)
	dc_description_positions=DcDescriptionPositionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_relation_IsPartOfSeriess=DcRelationIspartofseriesSerializer(many=True,read_only=True)
	dc_rightss=DcRightsSerializer(many=True,read_only=True)
	dc_rights_uris=DcRightsUriSerializer(many=True,read_only=True)
	dc_sources=DcSourceSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_adcats=DcSubjectAdcatSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dspace_iiif_enableds=DspaceIiifEnabledSerializer(many=True,read_only=True)
	chao_company_addresss=ChaoCompanyAddressSerializer(many=True,read_only=True)
	chao_company_names=ChaoCompanyNameSerializer(many=True,read_only=True)
	chao_company_nations=ChaoCompanyNationSerializer(many=True,read_only=True)
	chao_contributor_printers=ChaoContributorPrinterSerializer(many=True,read_only=True)
	chao_date_minguos=ChaoDateMinguoSerializer(many=True,read_only=True)
	chao_printer_cheifeditors=ChaoPrinterCheifeditorSerializer(many=True,read_only=True)
	chao_productagencys=ChaoProductagencySerializer(many=True,read_only=True)
	dc_citation_issueNumbers=DcCitationIssuenumberSerializer(many=True,read_only=True)
	dc_citation_pageNumbers=DcCitationPagenumberSerializer(many=True,read_only=True)
	dc_citation_volumeNumbers=DcCitationVolumenumberSerializer(many=True,read_only=True)
	dc_contributor_funders=DcContributorFunderSerializer(many=True,read_only=True)
	dc_contributor_publishers=DcContributorPublisherSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_digitals=DcDateDigitalSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_fulltexts=DcDescriptionFulltextSerializer(many=True,read_only=True)
	dc_description_positions=DcDescriptionPositionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_relation_IsPartOfSeriess=DcRelationIspartofseriesSerializer(many=True,read_only=True)
	dc_rightss=DcRightsSerializer(many=True,read_only=True)
	dc_rights_uris=DcRightsUriSerializer(many=True,read_only=True)
	dc_sources=DcSourceSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_adcats=DcSubjectAdcatSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dspace_iiif_enableds=DspaceIiifEnabledSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dspace_iiif_enableds=DspaceIiifEnabledSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dspace_iiif_enableds=DspaceIiifEnabledSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	class Meta:
		model=PublishedAdvertisement
		fields='__all__'

class StagedAdvertisementSerializer(serializers.ModelSerializer):
	chao_company_addresss=ChaoCompanyAddressSerializer(many=True,read_only=True)
	chao_company_names=ChaoCompanyNameSerializer(many=True,read_only=True)
	chao_company_nations=ChaoCompanyNationSerializer(many=True,read_only=True)
	chao_contributor_printers=ChaoContributorPrinterSerializer(many=True,read_only=True)
	chao_date_chineselunars=ChaoDateChineselunarSerializer(many=True,read_only=True)
	chao_date_minguos=ChaoDateMinguoSerializer(many=True,read_only=True)
	chao_printer_cheifeditors=ChaoPrinterCheifeditorSerializer(many=True,read_only=True)
	chao_productagencys=ChaoProductagencySerializer(many=True,read_only=True)
	dc_citation_pageNumbers=DcCitationPagenumberSerializer(many=True,read_only=True)
	dc_citation_volumeNumbers=DcCitationVolumenumberSerializer(many=True,read_only=True)
	dc_contributor_funders=DcContributorFunderSerializer(many=True,read_only=True)
	dc_contributor_publishers=DcContributorPublisherSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_digitals=DcDateDigitalSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_fulltexts=DcDescriptionFulltextSerializer(many=True,read_only=True)
	dc_description_positions=DcDescriptionPositionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_relation_IsPartOfSeriess=DcRelationIspartofseriesSerializer(many=True,read_only=True)
	dc_rightss=DcRightsSerializer(many=True,read_only=True)
	dc_rights_uris=DcRightsUriSerializer(many=True,read_only=True)
	dc_sources=DcSourceSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_adcats=DcSubjectAdcatSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	chao_company_addresss=ChaoCompanyAddressSerializer(many=True,read_only=True)
	chao_company_names=ChaoCompanyNameSerializer(many=True,read_only=True)
	chao_company_nations=ChaoCompanyNationSerializer(many=True,read_only=True)
	chao_contributor_printers=ChaoContributorPrinterSerializer(many=True,read_only=True)
	chao_date_chineselunars=ChaoDateChineselunarSerializer(many=True,read_only=True)
	chao_date_minguos=ChaoDateMinguoSerializer(many=True,read_only=True)
	chao_printer_cheifeditors=ChaoPrinterCheifeditorSerializer(many=True,read_only=True)
	chao_productagencys=ChaoProductagencySerializer(many=True,read_only=True)
	dc_citation_pageNumbers=DcCitationPagenumberSerializer(many=True,read_only=True)
	dc_citation_volumeNumbers=DcCitationVolumenumberSerializer(many=True,read_only=True)
	dc_contributor_funders=DcContributorFunderSerializer(many=True,read_only=True)
	dc_contributor_publishers=DcContributorPublisherSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_digitals=DcDateDigitalSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_fulltexts=DcDescriptionFulltextSerializer(many=True,read_only=True)
	dc_description_positions=DcDescriptionPositionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_relation_IsPartOfSeriess=DcRelationIspartofseriesSerializer(many=True,read_only=True)
	dc_rightss=DcRightsSerializer(many=True,read_only=True)
	dc_rights_uris=DcRightsUriSerializer(many=True,read_only=True)
	dc_sources=DcSourceSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_adcats=DcSubjectAdcatSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	chao_company_addresss=ChaoCompanyAddressSerializer(many=True,read_only=True)
	chao_company_names=ChaoCompanyNameSerializer(many=True,read_only=True)
	chao_company_nations=ChaoCompanyNationSerializer(many=True,read_only=True)
	chao_contributor_printers=ChaoContributorPrinterSerializer(many=True,read_only=True)
	chao_date_minguos=ChaoDateMinguoSerializer(many=True,read_only=True)
	chao_printer_cheifeditors=ChaoPrinterCheifeditorSerializer(many=True,read_only=True)
	chao_productagencys=ChaoProductagencySerializer(many=True,read_only=True)
	dc_citation_issueNumbers=DcCitationIssuenumberSerializer(many=True,read_only=True)
	dc_citation_pageNumbers=DcCitationPagenumberSerializer(many=True,read_only=True)
	dc_citation_volumeNumbers=DcCitationVolumenumberSerializer(many=True,read_only=True)
	dc_contributor_funders=DcContributorFunderSerializer(many=True,read_only=True)
	dc_contributor_publishers=DcContributorPublisherSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_digitals=DcDateDigitalSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_fulltexts=DcDescriptionFulltextSerializer(many=True,read_only=True)
	dc_description_positions=DcDescriptionPositionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_relation_IsPartOfSeriess=DcRelationIspartofseriesSerializer(many=True,read_only=True)
	dc_rightss=DcRightsSerializer(many=True,read_only=True)
	dc_rights_uris=DcRightsUriSerializer(many=True,read_only=True)
	dc_sources=DcSourceSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_adcats=DcSubjectAdcatSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dspace_iiif_enableds=DspaceIiifEnabledSerializer(many=True,read_only=True)
	chao_company_addresss=ChaoCompanyAddressSerializer(many=True,read_only=True)
	chao_company_names=ChaoCompanyNameSerializer(many=True,read_only=True)
	chao_company_nations=ChaoCompanyNationSerializer(many=True,read_only=True)
	chao_contributor_printers=ChaoContributorPrinterSerializer(many=True,read_only=True)
	chao_date_minguos=ChaoDateMinguoSerializer(many=True,read_only=True)
	chao_printer_cheifeditors=ChaoPrinterCheifeditorSerializer(many=True,read_only=True)
	chao_productagencys=ChaoProductagencySerializer(many=True,read_only=True)
	dc_citation_issueNumbers=DcCitationIssuenumberSerializer(many=True,read_only=True)
	dc_citation_pageNumbers=DcCitationPagenumberSerializer(many=True,read_only=True)
	dc_citation_volumeNumbers=DcCitationVolumenumberSerializer(many=True,read_only=True)
	dc_contributor_funders=DcContributorFunderSerializer(many=True,read_only=True)
	dc_contributor_publishers=DcContributorPublisherSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_digitals=DcDateDigitalSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_fulltexts=DcDescriptionFulltextSerializer(many=True,read_only=True)
	dc_description_positions=DcDescriptionPositionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_relation_IsPartOfSeriess=DcRelationIspartofseriesSerializer(many=True,read_only=True)
	dc_rightss=DcRightsSerializer(many=True,read_only=True)
	dc_rights_uris=DcRightsUriSerializer(many=True,read_only=True)
	dc_sources=DcSourceSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_adcats=DcSubjectAdcatSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dspace_iiif_enableds=DspaceIiifEnabledSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dspace_iiif_enableds=DspaceIiifEnabledSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dspace_iiif_enableds=DspaceIiifEnabledSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_createds=DcDateCreatedSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_format_mediums=DcFormatMediumSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodcats=DcSubjectProdcatSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_title_subtitles=DcTitleSubtitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	class Meta:
		model=StagedAdvertisement
		fields='__all__'

