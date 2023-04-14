# Generated by Django 4.2 on 2023-04-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaoCompanyAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'chao.company.address',
            },
        ),
        migrations.CreateModel(
            name='ChaoCompanyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'chao.company.name',
            },
        ),
        migrations.CreateModel(
            name='ChaoCompanyNation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'chao.company.nation',
            },
        ),
        migrations.CreateModel(
            name='ChaoContributorPrinter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'chao.contributor.printer',
            },
        ),
        migrations.CreateModel(
            name='ChaoDateChineselunar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'chao.date.chineselunar',
            },
        ),
        migrations.CreateModel(
            name='ChaoDateMinguo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'chao.date.minguo',
            },
        ),
        migrations.CreateModel(
            name='ChaoPrinterCheifeditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'chao.printer.cheifeditor',
            },
        ),
        migrations.CreateModel(
            name='ChaoProductagency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'chao.productagency',
            },
        ),
        migrations.CreateModel(
            name='DcCitationIssuenumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.citation.issueNumber',
            },
        ),
        migrations.CreateModel(
            name='DcCitationPagenumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.citation.pageNumber',
            },
        ),
        migrations.CreateModel(
            name='DcCitationVolumenumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.citation.volumeNumber',
            },
        ),
        migrations.CreateModel(
            name='DcContributorFunder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.contributor.funder',
            },
        ),
        migrations.CreateModel(
            name='DcContributorPublisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.contributor.publisher',
            },
        ),
        migrations.CreateModel(
            name='DcCoverageSpatial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.coverage.spatial',
            },
        ),
        migrations.CreateModel(
            name='DcDateAccessioned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.TextField(blank=True, null=True)),
                ('text_EN', models.TextField(blank=True, null=True)),
                ('text_CN', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'dc.date.accessioned',
            },
        ),
        migrations.CreateModel(
            name='DcDateAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.date.available',
            },
        ),
        migrations.CreateModel(
            name='DcDateCreated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.date.created',
            },
        ),
        migrations.CreateModel(
            name='DcDateDigital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.date.digital',
            },
        ),
        migrations.CreateModel(
            name='DcDateIssued',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.date.issued',
            },
        ),
        migrations.CreateModel(
            name='DcDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.description',
            },
        ),
        migrations.CreateModel(
            name='DcDescriptionFulltext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.description.fulltext',
            },
        ),
        migrations.CreateModel(
            name='DcDescriptionPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.description.position',
            },
        ),
        migrations.CreateModel(
            name='DcDescriptionProvenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.description.provenance',
            },
        ),
        migrations.CreateModel(
            name='DcDigitizationSpecifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.TextField(blank=True, null=True)),
                ('text_EN', models.TextField(blank=True, null=True)),
                ('text_CN', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'dc.digitization.specifications',
            },
        ),
        migrations.CreateModel(
            name='DcFormatMedium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.format.medium',
            },
        ),
        migrations.CreateModel(
            name='DcIdentifierDigital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.identifier.digital',
            },
        ),
        migrations.CreateModel(
            name='DcIdentifierUri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.identifier.uri',
            },
        ),
        migrations.CreateModel(
            name='DcLanguageIso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.language.iso',
            },
        ),
        migrations.CreateModel(
            name='DcPublisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.publisher',
            },
        ),
        migrations.CreateModel(
            name='DcRelationIspartofseries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.TextField(blank=True, null=True)),
                ('text_EN', models.TextField(blank=True, null=True)),
                ('text_CN', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'dc.relation.IsPartOfSeries',
            },
        ),
        migrations.CreateModel(
            name='DcRights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.rights',
            },
        ),
        migrations.CreateModel(
            name='DcRightsUri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.TextField(blank=True, null=True)),
                ('text_EN', models.TextField(blank=True, null=True)),
                ('text_CN', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'dc.rights.uri',
            },
        ),
        migrations.CreateModel(
            name='DcSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.source',
            },
        ),
        migrations.CreateModel(
            name='DcSourceCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.source.collection',
            },
        ),
        migrations.CreateModel(
            name='DcSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.subject',
            },
        ),
        migrations.CreateModel(
            name='DcSubjectAdcat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.subject.adcat',
            },
        ),
        migrations.CreateModel(
            name='DcSubjectBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.subject.brand',
            },
        ),
        migrations.CreateModel(
            name='DcSubjectProdcat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.subject.prodcat',
            },
        ),
        migrations.CreateModel(
            name='DcSubjectProdtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.subject.prodtype',
            },
        ),
        migrations.CreateModel(
            name='DcTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.title',
            },
        ),
        migrations.CreateModel(
            name='DcTitleSubtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.TextField(blank=True, null=True)),
                ('text_EN', models.TextField(blank=True, null=True)),
                ('text_CN', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'dc.title.subtitle',
            },
        ),
        migrations.CreateModel(
            name='DcTypeDcmi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.type.dcmi',
            },
        ),
        migrations.CreateModel(
            name='DcTypeGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dc.type.genre',
            },
        ),
        migrations.CreateModel(
            name='DspaceIiifEnabled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_original', models.CharField(blank=True, max_length=500, null=True)),
                ('text_EN', models.CharField(blank=True, max_length=500, null=True)),
                ('text_CN', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'dspace.iiif.enabled',
            },
        ),
    ]