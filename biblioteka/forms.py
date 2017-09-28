from django.contrib.auth.forms import UserCreationForm

from korisnik.models import Korisnik
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    datum_rodjenja = forms.DateField(help_text='Obavezno. Format: YYYY-MM-DD', label='Datum rodjenja :')
    adresa = forms.CharField(help_text="Unesite vasu adresu", label="Adresa :")

    class Meta:
        model = User
        fields = ('username', 'datum_rodjenja', 'password1', 'password2','first_name','last_name', 'email' )