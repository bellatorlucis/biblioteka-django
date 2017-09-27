from django import forms
from korisnik.models import Knjiga, Zaduzenje,Korisnik
from django.contrib.auth.models import User

class KnjigaCreateForm(forms.ModelForm):

    class Meta:
        model = Knjiga
        fields = '__all__'


class ZaduzenjeCreateForm(forms.ModelForm):
    korisnik = forms.ModelChoiceField(queryset=Korisnik.objects.filter(user__groups__name='korisnik'))
    class Meta:
        model = Zaduzenje
        fields = '__all__'