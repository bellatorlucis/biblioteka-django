# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import korisnik.models


class Migration(migrations.Migration):

    dependencies = [
        ('korisnik', '0004_auto_20170925_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='knjiga',
            name='slika',
            field=models.ImageField(blank=True, null=True, upload_to=korisnik.models.get_image_path),
        ),
    ]
