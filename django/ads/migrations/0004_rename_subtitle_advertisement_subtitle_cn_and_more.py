# Generated by Django 4.0 on 2022-11-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_advertisement_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='subtitle',
            new_name='subtitle_CN',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='subtitle_EN',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]