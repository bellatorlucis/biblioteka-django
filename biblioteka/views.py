from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, RequestContext
from django.views import View
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied

from biblioteka import settings
from biblioteka.forms import SignUpForm
from django.contrib.auth.models import Group

@login_required()
def login_success(request):
    if request.user.groups.filter(name="korisnik").exists():
        return redirect(settings.KORISNIK_MAIN_URL)
    elif request.user.groups.filter(name="sluzbenik").exists():
        return redirect(settings.SLUZBENIK_MAIN_URL)
    else:
        raise PermissionDenied

class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password= password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('/login-success')
            else:
                return HttpResponse("Inactive user.")
        else:
            messages.error(request, "Pogresno ste uneli username ili password")
            return redirect(settings.LOGIN_URL)

class LogOutView(View):

    def get(self, request):
        logout(request)
        context = {
            'nottification' : 'Uspseno ste se izlogovali !'
        }
        return redirect(settings.LOGIN_URL, context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            group = Group.objects.get(name='korisnik')
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.korisnik.datum_rodjenja = form.cleaned_data.get('datum_rodjenja')
            user.groups.add(group)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login-success')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})

class SignUpView(TemplateView):
    template_name = 'registration.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['form'] = SignUpForm()
        return context

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            group = Group.objects.get(name='korisnik')
            user = form.save()
            user.refresh_from_db()
            user.korisnik.datum_rodjenja = form.cleaned_data.get('datum_rodjenja')
            user.groups.add(group)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login-success')



class BibliotekaHome(TemplateView):
    template_name = 'index.html'
