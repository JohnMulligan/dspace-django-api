# Generated by Django 4.2 on 2023-04-12 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0018_advertisement_description_fulltext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='uid',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='mediatype',
            unique_together={('name_EN', 'name_CN')},
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together={('name_EN', 'name_CN')},
        ),
        migrations.AlterUniqueTogether(
            name='productcategory',
            unique_together={('name_EN', 'name_CN')},
        ),
        migrations.AlterUniqueTogether(
            name='producttype',
            unique_together={('name_EN', 'name_CN')},
        ),
        migrations.AlterUniqueTogether(
            name='subject',
            unique_together={('name_EN', 'name_CN')},
        ),
    ]
