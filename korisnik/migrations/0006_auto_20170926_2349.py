# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('korisnik', '0005_knjiga_slika'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knjiga',
            name='slika',
            field=models.ImageField(blank=True, null=True, upload_to='knjige/'),
        ),
        migrations.AlterField(
            model_name='zaduzenje',
            name='korisnik',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='korisnik.Korisnik'),
        ),
        migrations.AlterField(
            model_name='zaduzenje',
            name='primerak',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='korisnik.Primerak'),
        ),
    ]