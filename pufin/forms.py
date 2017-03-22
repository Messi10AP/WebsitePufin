from django import forms
from django.forms import ModelForm
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime

class RegisterForm(forms.Form):
    GRADE_CHOICES = ( 
                (1,'Yes'), (0,'No'), 
            )
    Orig_Platform = forms.CharField(max_length = 25)
    Orig_Loanid = forms.CharField( max_length = 25)
    Orig_Loanamount = forms.CharField( max_length = 25)
    Orig_Loandate = forms.CharField( max_length = 25)
    Published = forms.ChoiceField(choices=GRADE_CHOICES)
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        print cleaned_data   
        return cleaned_data

