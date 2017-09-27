from django.conf.urls import url, include
from django.contrib import admin
from korisnik import views as korisnik_views
from django.conf.urls.static import static
from biblioteka import settings

urlpatterns=[
    url(r'^$', korisnik_views.HomePageKorisnik.as_view(), name="korisnik-home"),
    url(r'^knjiga/zaduzene/', korisnik_views.KorisnikSveZaduzeneKnjigeView.as_view(), name='korisnik-sve-zaduzene-knjige'),
    url(r'^knjiga/sve', korisnik_views.KorisnikSveKnjigeView.as_view(), name='korisnik-sve-knjige'),
    url(r'knjiga/zaduzi/', korisnik_views.ZaduziKnjiguView.as_view(), name='korisnik-zaduzi-knjigu'),
    url(r'knjiga/pretraga', korisnik_views.PretragaKnjigaView.as_view(), name='korisnik-pretraga-knjiga')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)