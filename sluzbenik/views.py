from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, DetailView, CreateView, ListView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from biblioteka_mixins.SluzbenikGroupRequiredMixin import SluzbenikGroupRequiredMixin
from .forms import KnjigaCreateForm, ZaduzenjeCreateForm
from korisnik.models import Knjiga, Zaduzenje, Korisnik, Primerak
from datetime import date
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


class SluzbenikHomeView(LoginRequiredMixin, SluzbenikGroupRequiredMixin, TemplateView):
    template_name = 'sluzbenik/home.html'

    def get_context_data(self, **kwargs):
        context = super(SluzbenikHomeView, self).get_context_data(**kwargs)
        context['korisnik'] = self.request.user.korisnik
        return context

class CreateKnjigaView(LoginRequiredMixin, SluzbenikGroupRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'sluzbenik/add_knjiga.html'
    model = Knjiga
    form_class = KnjigaCreateForm
    success_url = 'add-knjiga'

    def form_valid(self, form):
        self.object = form.save()
        knjiga = self.object
        broj_primeraka = int(self.request.POST['broj_primeraka'])
        for x in range(0, broj_primeraka):
            primerak = Primerak()
            primerak.knjiga = knjiga
            primerak.save()

        messages.success(self.request, "USpesno dodata knjiga!")
        return redirect(self.get_success_url())



class DeleteKnjigaView(LoginRequiredMixin, SluzbenikGroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Knjiga
    success_url = reverse_lazy('knjiga-sve')
    template_name = 'sluzbenik/knjiga_delete_confirmation.html'
    success_message = 'Uspesno obrisana knjiga'

class KnjigeSveView(LoginRequiredMixin,SluzbenikGroupRequiredMixin,ListView):
    model = Knjiga
    template_name = 'sluzbenik/sve_knjige.html'
    context_object_name = 'knjige'

class KnjigaDetailView(LoginRequiredMixin, SluzbenikGroupRequiredMixin, SuccessMessageMixin, DetailView):
    template_name = 'sluzbenik/knjiga_detail.html'
    context_object_name = 'knjiga'
    model = Knjiga

    def get_context_data(self, **kwargs):
        context = super(KnjigaDetailView, self).get_context_data(**kwargs)
        knjiga_id = self.kwargs['pk']
        zaduzenja = Zaduzenje.objects.filter(primerak__knjiga_id=knjiga_id).filter(datum_vracanja=None)
        print(zaduzenja)
        context['zaduzenja'] = zaduzenja
        return context

class PretragaKnjigaView(LoginRequiredMixin, SluzbenikGroupRequiredMixin, SuccessMessageMixin, ListView):
    template_name = 'sluzbenik/pretraga-knjiga.html'
    context_object_name = 'knjige'
    model = Knjiga

    def get_queryset(self):
        search_str = self.request.GET['search_string']
        knjige= Knjiga.objects.filter(naziv__icontains=search_str)

        return knjige

class CreateZaduzenjeView(LoginRequiredMixin, SluzbenikGroupRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'sluzbenik/add_zaduzenje.html'
    model = Zaduzenje
    form_class = ZaduzenjeCreateForm
    success_url = 'add-zaduzenje'
    success_message = 'Uspesno dodato zaduzenje'


class KorisnikDetailView(LoginRequiredMixin, SluzbenikGroupRequiredMixin,DetailView):
    template_name = 'sluzbenik/korisnik_detail.html'
    model = Korisnik
    context_object_name = 'korisnik'

    def get_context_data(self, **kwargs):
        context = super(KorisnikDetailView, self).get_context_data(**kwargs)
        korisnik_id = self.kwargs['pk']
        korisnik = Korisnik.objects.get(pk=korisnik_id)
        zaduzenja = Zaduzenje.objects.filter(korisnik=korisnik).filter(datum_vracanja=None)
        context['zaduzenja'] = zaduzenja
        print(zaduzenja)
        return context

class KorisniciSviView(LoginRequiredMixin,SluzbenikGroupRequiredMixin,ListView):
    model = Korisnik
    template_name = 'sluzbenik/svi_korisnici.html'
    context_object_name = 'korisnici'

    def get_queryset(self):
        korisnici = Korisnik.objects.filter(user__groups__name='korisnik')

        return korisnici


class KorisnikDeleteView(LoginRequiredMixin, SluzbenikGroupRequiredMixin, DeleteView):
    model = User
    context_object_name = 'user'
    template_name = 'sluzbenik/korisnik_delete_confirmation.html'
    success_url = reverse_lazy('korisnik-svi')
    success_message = 'Uspesno obrisan korisnik'


class RazduziView(LoginRequiredMixin,SluzbenikGroupRequiredMixin,SuccessMessageMixin, View):

    def get(self,request, id, knjiga_id):
        zaduzenje = Zaduzenje.objects.get(pk=id)
        zaduzenje.datum_vracanja = date.today()
        zaduzenje.save()
        messages.success(request, 'Uspesno razduzena knjiga !')

        return redirect('knjiga-details', pk =knjiga_id)

class Success(LoginRequiredMixin, SluzbenikGroupRequiredMixin, TemplateView):
    template_name = 'sluzbenik/success.html'
