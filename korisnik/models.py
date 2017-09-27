from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

def get_image_path(instance, filename):
    return os.path.join('knjige', str(instance.id), filename)


class Korisnik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    datum_rodjenja = models.DateField(blank=True, null=True)
    adresa = models.CharField(max_length=256, blank=True, default="prazno")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Korisnik.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.korisnik.save()


    def __str__(self):
        return self.user.first_name + self.user.last_name

class Knjiga(models.Model):
    naziv = models.CharField(max_length=256, default="prazno")
    autor = models.CharField(max_length=256, default="prazno")
    slika = models.ImageField(upload_to='knjige/', blank=True, null=True)

    def __str__(self):
        return self.naziv + self.autor

class Primerak(models.Model):
    knjiga = models.ForeignKey(Knjiga, on_delete=models.CASCADE)
    korisnik = models.ManyToManyField(Korisnik, through='Zaduzenje')

    def __str__(self):
        return self.knjiga.naziv + self.knjiga.autor + " "+ str(self.pk)


class Zaduzenje(models.Model):
    datun_iznajmljivanja = models.DateField(auto_now_add=True)
    datum_vracanja = models.DateField(blank=True, null=True)
    primerak = models.ForeignKey(Primerak, on_delete=models.CASCADE)
    korisnik = models.ForeignKey(Korisnik, on_delete=models.CASCADE)





