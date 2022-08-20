from django.shortcuts import render

from django import forms
# Create your views here.

class ContactForm(forms.Form) :
    nama = forms.CharField()
    noHp = forms.CharField()
def index(request):
    contact_nama = ContactForm()
    contact_noHp = ContactForm()
    content= {
        'halaman' : 'contact',
        'contact_nama' : contact_nama,
        'contact_noHp' : contact_noHp
    }
    return render(request, 'contact/index.html', content)