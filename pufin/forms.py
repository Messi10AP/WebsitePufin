from django import forms
from django.forms import ModelForm
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import UserInfo, Payment
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime
class RegisterForm(forms.Form):
    GRADE_CHOICES = ( 
                (9,'9'), (10,'10'), (11,'11'), (12,'12') , 
            )
    curr_year = date.today().year
    if date.today().month > 6:
        curr_year=curr_year+1
    GRAD_YEAR_CHOICES = ( 
                (curr_year,curr_year), (curr_year+1,curr_year+1), (curr_year+2,curr_year+2), (curr_year+3,curr_year+3) , 
                 )
    first_name = forms.CharField(max_length = 25)
    username = forms.CharField(max_length = 25)
    last_name = forms.CharField( max_length = 25)
    emailid = forms.EmailField()
    passwd1 = forms.CharField(max_length=100,widget=forms.PasswordInput)
    passwd2 = forms.CharField(max_length=100,widget=forms.PasswordInput)
    gradyear = forms.ChoiceField( choices=GRAD_YEAR_CHOICES)
    grade = forms.ChoiceField( choices=GRADE_CHOICES)
    pin = forms.DecimalField(max_digits=4, decimal_places=0)
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        print cleaned_data   
        return cleaned_data

