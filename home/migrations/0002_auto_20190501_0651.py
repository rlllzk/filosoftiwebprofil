# Generated by Django 2.2 on 2019-05-01 06:51

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='ifoto',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='services',
            name='sfoto',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='works',
            name='wfoto',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
