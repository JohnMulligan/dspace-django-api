# Generated by Django 4.2 on 2023-04-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_stagedphoto_parent_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='stagedphoto',
            name='filename',
            field=models.CharField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stagedadvertisement',
            name='tmp_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
