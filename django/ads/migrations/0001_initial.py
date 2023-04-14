# Generated by Django 4.2 on 2023-04-13 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('dspace_uri', models.URLField(blank=True, max_length=250)),
                ('parent_collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.collection')),
            ],
        ),
        migrations.CreateModel(
            name='StagedAdvertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_year', models.IntegerField(blank=True, null=True)),
                ('tmp_name', models.CharField(max_length=50, unique=True)),
                ('chao_company_addresss', models.ManyToManyField(to='metadata.chaocompanyaddress')),
                ('chao_company_names', models.ManyToManyField(to='metadata.chaocompanyname')),
                ('chao_company_nations', models.ManyToManyField(to='metadata.chaocompanynation')),
                ('chao_contributor_printers', models.ManyToManyField(to='metadata.chaocontributorprinter')),
                ('chao_date_chineselunars', models.ManyToManyField(to='metadata.chaodatechineselunar')),
                ('chao_date_minguos', models.ManyToManyField(to='metadata.chaodateminguo')),
                ('chao_printer_cheifeditors', models.ManyToManyField(to='metadata.chaoprintercheifeditor')),
                ('chao_productagencys', models.ManyToManyField(to='metadata.chaoproductagency')),
                ('dc_citation_issueNumbers', models.ManyToManyField(to='metadata.dccitationissuenumber')),
                ('dc_citation_pageNumbers', models.ManyToManyField(to='metadata.dccitationpagenumber')),
                ('dc_citation_volumeNumbers', models.ManyToManyField(to='metadata.dccitationvolumenumber')),
                ('dc_contributor_funders', models.ManyToManyField(to='metadata.dccontributorfunder')),
                ('dc_contributor_publishers', models.ManyToManyField(to='metadata.dccontributorpublisher')),
                ('dc_coverage_spatials', models.ManyToManyField(to='metadata.dccoveragespatial')),
                ('dc_date_accessioneds', models.ManyToManyField(to='metadata.dcdateaccessioned')),
                ('dc_date_availables', models.ManyToManyField(to='metadata.dcdateavailable')),
                ('dc_date_createds', models.ManyToManyField(to='metadata.dcdatecreated')),
                ('dc_date_digitals', models.ManyToManyField(to='metadata.dcdatedigital')),
                ('dc_date_issueds', models.ManyToManyField(to='metadata.dcdateissued')),
                ('dc_description_fulltexts', models.ManyToManyField(to='metadata.dcdescriptionfulltext')),
                ('dc_description_positions', models.ManyToManyField(to='metadata.dcdescriptionposition')),
                ('dc_description_provenances', models.ManyToManyField(to='metadata.dcdescriptionprovenance')),
                ('dc_descriptions', models.ManyToManyField(to='metadata.dcdescription')),
                ('dc_digitization_specificationss', models.ManyToManyField(to='metadata.dcdigitizationspecifications')),
                ('dc_format_mediums', models.ManyToManyField(to='metadata.dcformatmedium')),
                ('dc_identifier_digitals', models.ManyToManyField(to='metadata.dcidentifierdigital')),
                ('dc_identifier_uris', models.ManyToManyField(to='metadata.dcidentifieruri')),
                ('dc_language_isos', models.ManyToManyField(to='metadata.dclanguageiso')),
                ('dc_publishers', models.ManyToManyField(to='metadata.dcpublisher')),
                ('dc_relation_IsPartOfSeriess', models.ManyToManyField(to='metadata.dcrelationispartofseries')),
                ('dc_rights_uris', models.ManyToManyField(to='metadata.dcrightsuri')),
                ('dc_rightss', models.ManyToManyField(to='metadata.dcrights')),
                ('dc_source_collections', models.ManyToManyField(to='metadata.dcsourcecollection')),
                ('dc_sources', models.ManyToManyField(to='metadata.dcsource')),
                ('dc_subject_adcats', models.ManyToManyField(to='metadata.dcsubjectadcat')),
                ('dc_subject_brands', models.ManyToManyField(to='metadata.dcsubjectbrand')),
                ('dc_subject_prodcats', models.ManyToManyField(to='metadata.dcsubjectprodcat')),
                ('dc_subject_prodtypes', models.ManyToManyField(to='metadata.dcsubjectprodtype')),
                ('dc_subjects', models.ManyToManyField(to='metadata.dcsubject')),
                ('dc_title_subtitles', models.ManyToManyField(to='metadata.dctitlesubtitle')),
                ('dc_titles', models.ManyToManyField(to='metadata.dctitle')),
                ('dc_type_dcmis', models.ManyToManyField(to='metadata.dctypedcmi')),
                ('dc_type_genres', models.ManyToManyField(to='metadata.dctypegenre')),
                ('dspace_iiif_enableds', models.ManyToManyField(to='metadata.dspaceiiifenabled')),
                ('owning_collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.collection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StagedPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staged_photo', models.FileField(blank=True, null=True, upload_to='staged_photos/')),
                ('parent_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.stagedadvertisement')),
            ],
        ),
        migrations.CreateModel(
            name='PublishedAdvertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_year', models.IntegerField(blank=True, null=True)),
                ('uuid', models.CharField(max_length=50, unique=True)),
                ('dspace_uri', models.URLField(blank=True, max_length=250, null=True)),
                ('dspace_iiif_uri', models.URLField(blank=True, max_length=250, null=True)),
                ('iiif_enabled', models.BooleanField(default=False)),
                ('is_current', models.BooleanField(default=False)),
                ('chao_company_addresss', models.ManyToManyField(to='metadata.chaocompanyaddress')),
                ('chao_company_names', models.ManyToManyField(to='metadata.chaocompanyname')),
                ('chao_company_nations', models.ManyToManyField(to='metadata.chaocompanynation')),
                ('chao_contributor_printers', models.ManyToManyField(to='metadata.chaocontributorprinter')),
                ('chao_date_chineselunars', models.ManyToManyField(to='metadata.chaodatechineselunar')),
                ('chao_date_minguos', models.ManyToManyField(to='metadata.chaodateminguo')),
                ('chao_printer_cheifeditors', models.ManyToManyField(to='metadata.chaoprintercheifeditor')),
                ('chao_productagencys', models.ManyToManyField(to='metadata.chaoproductagency')),
                ('dc_citation_issueNumbers', models.ManyToManyField(to='metadata.dccitationissuenumber')),
                ('dc_citation_pageNumbers', models.ManyToManyField(to='metadata.dccitationpagenumber')),
                ('dc_citation_volumeNumbers', models.ManyToManyField(to='metadata.dccitationvolumenumber')),
                ('dc_contributor_funders', models.ManyToManyField(to='metadata.dccontributorfunder')),
                ('dc_contributor_publishers', models.ManyToManyField(to='metadata.dccontributorpublisher')),
                ('dc_coverage_spatials', models.ManyToManyField(to='metadata.dccoveragespatial')),
                ('dc_date_accessioneds', models.ManyToManyField(to='metadata.dcdateaccessioned')),
                ('dc_date_availables', models.ManyToManyField(to='metadata.dcdateavailable')),
                ('dc_date_createds', models.ManyToManyField(to='metadata.dcdatecreated')),
                ('dc_date_digitals', models.ManyToManyField(to='metadata.dcdatedigital')),
                ('dc_date_issueds', models.ManyToManyField(to='metadata.dcdateissued')),
                ('dc_description_fulltexts', models.ManyToManyField(to='metadata.dcdescriptionfulltext')),
                ('dc_description_positions', models.ManyToManyField(to='metadata.dcdescriptionposition')),
                ('dc_description_provenances', models.ManyToManyField(to='metadata.dcdescriptionprovenance')),
                ('dc_descriptions', models.ManyToManyField(to='metadata.dcdescription')),
                ('dc_digitization_specificationss', models.ManyToManyField(to='metadata.dcdigitizationspecifications')),
                ('dc_format_mediums', models.ManyToManyField(to='metadata.dcformatmedium')),
                ('dc_identifier_digitals', models.ManyToManyField(to='metadata.dcidentifierdigital')),
                ('dc_identifier_uris', models.ManyToManyField(to='metadata.dcidentifieruri')),
                ('dc_language_isos', models.ManyToManyField(to='metadata.dclanguageiso')),
                ('dc_publishers', models.ManyToManyField(to='metadata.dcpublisher')),
                ('dc_relation_IsPartOfSeriess', models.ManyToManyField(to='metadata.dcrelationispartofseries')),
                ('dc_rights_uris', models.ManyToManyField(to='metadata.dcrightsuri')),
                ('dc_rightss', models.ManyToManyField(to='metadata.dcrights')),
                ('dc_source_collections', models.ManyToManyField(to='metadata.dcsourcecollection')),
                ('dc_sources', models.ManyToManyField(to='metadata.dcsource')),
                ('dc_subject_adcats', models.ManyToManyField(to='metadata.dcsubjectadcat')),
                ('dc_subject_brands', models.ManyToManyField(to='metadata.dcsubjectbrand')),
                ('dc_subject_prodcats', models.ManyToManyField(to='metadata.dcsubjectprodcat')),
                ('dc_subject_prodtypes', models.ManyToManyField(to='metadata.dcsubjectprodtype')),
                ('dc_subjects', models.ManyToManyField(to='metadata.dcsubject')),
                ('dc_title_subtitles', models.ManyToManyField(to='metadata.dctitlesubtitle')),
                ('dc_titles', models.ManyToManyField(to='metadata.dctitle')),
                ('dc_type_dcmis', models.ManyToManyField(to='metadata.dctypedcmi')),
                ('dc_type_genres', models.ManyToManyField(to='metadata.dctypegenre')),
                ('dspace_iiif_enableds', models.ManyToManyField(to='metadata.dspaceiiifenabled')),
                ('owning_collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.collection')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
