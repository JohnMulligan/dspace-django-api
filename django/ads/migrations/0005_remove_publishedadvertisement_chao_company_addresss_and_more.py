# Generated by Django 4.2 on 2023-04-14 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_stagedadvertisement_review_begun_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishedadvertisement',
            name='chao_company_addresss',
        ),
        migrations.RemoveField(
            model_name='publishedadvertisement',
            name='chao_company_names',
        ),
        migrations.RemoveField(
            model_name='publishedadvertisement',
            name='chao_company_nations',
        ),
        migrations.RemoveField(
            model_name='publishedadvertisement',
            name='chao_contributor_printers',
        ),
        migrations.RemoveField(
            model_name='publishedadvertisement',
            name='chao_date_chineselunars',
        ),
        migrations.RemoveField(
            model_name='publishedadvertisement',
            name='chao_date_minguos',
        ),
        migrations.RemoveField(
            model_name='publishedadvertisement',
            name='chao_printer_cheifeditors',
        ),
        migrations.RemoveField(
            model_name='publishedadvertisement',
            name='chao_productagencys',
        ),
        migrations.RemoveField(
            model_name='stagedadvertisement',
            name='chao_company_addresss',
        ),
        migrations.RemoveField(
            model_name='stagedadvertisement',
            name='chao_company_names',
        ),
        migrations.RemoveField(
            model_name='stagedadvertisement',
            name='chao_company_nations',
        ),
        migrations.RemoveField(
            model_name='stagedadvertisement',
            name='chao_contributor_printers',
        ),
        migrations.RemoveField(
            model_name='stagedadvertisement',
            name='chao_date_chineselunars',
        ),
        migrations.RemoveField(
            model_name='stagedadvertisement',
            name='chao_date_minguos',
        ),
        migrations.RemoveField(
            model_name='stagedadvertisement',
            name='chao_printer_cheifeditors',
        ),
        migrations.RemoveField(
            model_name='stagedadvertisement',
            name='chao_productagencys',
        ),
    ]
