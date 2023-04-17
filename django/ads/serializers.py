from rest_framework import serializers
from .models import *
from metadata.models import *

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

class PublishedAdvertisementSerializer(serializers.ModelSerializer):
	dc_coverage_spatials=DcCoverageSpatialSerializer(many=True,read_only=True)
	dc_date_accessioneds=DcDateAccessionedSerializer(many=True,read_only=True)
	dc_date_availables=DcDateAvailableSerializer(many=True,read_only=True)
	dc_date_issueds=DcDateIssuedSerializer(many=True,read_only=True)
	dc_descriptions=DcDescriptionSerializer(many=True,read_only=True)
	dc_description_fulltexts=DcDescriptionFulltextSerializer(many=True,read_only=True)
	dc_description_provenances=DcDescriptionProvenanceSerializer(many=True,read_only=True)
	dc_digitization_specificationss=DcDigitizationSpecificationsSerializer(many=True,read_only=True)
	dc_identifier_digitals=DcIdentifierDigitalSerializer(many=True,read_only=True)
	dc_identifier_uris=DcIdentifierUriSerializer(many=True,read_only=True)
	dc_language_isos=DcLanguageIsoSerializer(many=True,read_only=True)
	dc_publishers=DcPublisherSerializer(many=True,read_only=True)
	dc_source_collections=DcSourceCollectionSerializer(many=True,read_only=True)
	dc_subjects=DcSubjectSerializer(many=True,read_only=True)
	dc_subject_brands=DcSubjectBrandSerializer(many=True,read_only=True)
	dc_subject_prodtypes=DcSubjectProdtypeSerializer(many=True,read_only=True)
	dc_titles=DcTitleSerializer(many=True,read_only=True)
	dc_type_dcmis=DcTypeDcmiSerializer(many=True,read_only=True)
	dc_type_genres=DcTypeGenreSerializer(many=True,read_only=True)
	class Meta:
		model=PublishedAdvertisement
		fields='__all__'