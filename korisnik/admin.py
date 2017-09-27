from django.contrib import admin
from korisnik.models import Korisnik, Knjiga, Primerak, Zaduzenje

admin.site.register(Korisnik)
admin.site.register(Knjiga)
admin.site.register(Primerak)
admin.site.register(Zaduzenje)
# Register your models here.
