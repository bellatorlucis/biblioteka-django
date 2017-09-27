from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from biblioteka_mixins.KorisnikGroupRequiredMixin import KorisnikGroupRequiredMixin



class HomePageKorisnik(LoginRequiredMixin,KorisnikGroupRequiredMixin, TemplateView):
    template_name = 'korisnik/home.html'