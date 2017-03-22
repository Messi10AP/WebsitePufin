from django import forms
from django.forms import ModelForm
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length = 25)
    last_name = forms.CharField( max_length = 25)
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        print cleaned_data   
        return cleaned_data

