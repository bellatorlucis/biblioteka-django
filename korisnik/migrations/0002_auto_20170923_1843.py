# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korisnik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korisnik',
            name='datum_rodjenja',
            field=models.DateTimeField(),
        ),
    ]
