from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, DetailView, ListView
from django.contrib.auth.mixins import  LoginRequiredMixin
from biblioteka_mixins.KorisnikGroupRequiredMixin import KorisnikGroupRequiredMixin
from .models import Knjiga, Korisnik,Primerak, Zaduzenje
from datetime import date
from django.urls import reverse_lazy

class HomePageKorisnik(LoginRequiredMixin,KorisnikGroupRequiredMixin, TemplateView):
    template_name = 'korisnik/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageKorisnik, self).get_context_data(**kwargs)
        context['korisnik'] = self.request.user.korisnik
        korisnik = self.request.user.korisnik
        zaduzenja = Zaduzenje.objects.filter(korisnik=korisnik).filter(datum_vracanja=None)
        context['zaduzenja'] = zaduzenja
        return context

class KorisnikSveZaduzeneKnjigeView(LoginRequiredMixin, KorisnikGroupRequiredMixin, ListView):
    model = Zaduzenje
    context_object_name = 'zaduzenja'
    template_name = 'korisnik/sve_knjige_korisnika.html'

    def get_queryset(self):
        korisnik = self.request.user.korisnik
        zaduzenja =  Zaduzenje.objects.filter(korisnik=korisnik).filter(datum_vracanja=None)

        return zaduzenja

class KorisnikSveKnjigeView(LoginRequiredMixin,KorisnikGroupRequiredMixin, SuccessMessageMixin, ListView):
    model = Primerak
    context_object_name = 'primerci'
    template_name = 'korisnik/sve_knjige.html'

    def get_queryset(self):
        primerci = Primerak.objects.filter(zaduzenje=None)
        return primerci

class ZaduziKnjiguView(LoginRequiredMixin, KorisnikGroupRequiredMixin, View):

    def post(self, request):
        korisnik = request.user.korisnik
        primerak_id = request.POST['primerak_id'];
        primerak = Primerak.objects.get(pk=primerak_id)
        zaduznje = Zaduzenje()
        zaduznje.primerak = primerak
        zaduznje.korisnik = korisnik
        zaduznje.datun_iznajmljivanja = date.today()
        zaduznje.save()
        messages.success(request=request, message="Uspesno zaduzena knjiga")

        return redirect('korisnik-sve-knjige')

class PretragaKnjigaView(LoginRequiredMixin, KorisnikGroupRequiredMixin, SuccessMessageMixin, ListView):
    template_name = 'korisnik/pretraga-knjige.html'
    context_object_name = 'primerci'
    model = Primerak

    def get_queryset(self):
        search_str = self.request.GET['search_string']
        primerci = Primerak.objects.filter(knjiga__naziv__icontains=search_str).filter(zaduzenje__datum_vracanja=None)


        return primerci



class KnjigaDetailView(LoginRequiredMixin,KorisnikGroupRequiredMixin,SuccessMessageMixin, DetailView):
    model = Knjiga
    context_object_name = 'knjiga'

