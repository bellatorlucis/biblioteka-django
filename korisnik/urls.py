from django.conf.urls import url, include
from django.contrib import admin
from korisnik import views as korisnik_views
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', korisnik_views.HomePageKorisnik.as_view(), name="korisnik-home"),

]