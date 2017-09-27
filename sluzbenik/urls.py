from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from biblioteka import settings
from sluzbenik import views as sluzbenik_views
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', sluzbenik_views.SluzbenikHomeView.as_view(), name="sluzbenik-home"),
    url(r'^addKnjiga/', sluzbenik_views.CreateKnjigaView.as_view(), name='add-knjiga'),
    url(r'^addZaduzenje/', sluzbenik_views.CreateZaduzenjeView.as_view(), name='add-zaduzenje'),
    url(r'success/', sluzbenik_views.Success.as_view(),name='success'),
    url(r'^knjiga/detail/(?P<pk>[0-9]+)', sluzbenik_views.KnjigaDetailView.as_view(), name='knjiga-details'),
    url(r'^knjiga/razduzi/(?P<id>[0-9]+)/(?P<knjiga_id>[0-9]+)',sluzbenik_views.RazduziView.as_view(), name='knjiga-razduzi'),
    url(r'^knjiga/delte/(?P<pk>[0-9]+)', sluzbenik_views.DeleteKnjigaView.as_view(), name='knjiga-delete'),
    url(r'^knjiga/sve', sluzbenik_views.KnjigeSveView.as_view(), name='knjiga-sve'),
    url(r'^korisnik/detail/(?P<pk>[0-9]+)', sluzbenik_views.KorisnikDetailView.as_view(), name='korisnik-detail'),
    url(r'^korisnik/svi',sluzbenik_views.KorisniciSviView.as_view(), name='korisnik-svi' ),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

