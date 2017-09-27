#! /bin/bash

python3 manage.py runserver 192.168.1.3:7000

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Korisnik(models.Model):
    user : models.OneToOneField(User, on_delete=models.CASCADE)
    ime : models.CharField(max_length=50, blank=False)
    prezime : models.CharField(max_length=100)
    uloga : models.CharField(max_length=256, blank=False)
    datum_rodjenja : models.DateTimeField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Korisnik.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.korisnik.save()


    def __str__(self):
        return self.ime + self.prezime + self.datum_rodjenja

class Knjiga(models.Model):
    naziv : models.CharField(max_length=256)
    autor : models.CharField(max_length=256)
    izdavac : models.CharField(max_length=256)

    def __str__(self):
        return self.naziv + self.autor

class Primerak(models.Model):
    knjiga : models.ForeignKey(Knjiga, on_delete=models.CASCADE)
    korisnik : models.ManyToManyField(Korisnik, through='Zaduzenje')


class Zaduzenje(models.Model):
    datun_iznajmljivanja : models.DateField()
    datum_vracanja : models.DateField()
    primerak : models.ForeignKey(Primerak, on_delete=models.CASCADE)
    korisnik : models.ForeignKey(Korisnik, on_delete=models.CASCADE)