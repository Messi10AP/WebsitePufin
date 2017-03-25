from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls import url
from .models import UserInfo
from .forms import RegisterForm
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.db.models import Max, Sum
from datetime import date, timedelta
from django.core.urlresolvers import reverse
from django.shortcuts import render
import time
from datetime import datetime
import hashlib
import sys
@csrf_exempt
def Form(request):
    #deleteevent()
    print "signup"
    print "ASDASD"
    if request.method == 'POST':
        print "post signup"
        form = RegisterForm(request.POST, request.FILES)
        try:
            if form.is_valid():
     	        text=""
	        for chunk in request.FILES['upload'].chunks():
		    text += (chunk)
		sha256 = hashlib.sha256()
		sha256.update(text)
		HASH = sha256.hexdigest()
                a = UserInfo(Orig_Platform = form.cleaned_data['Orig_Platform'], Orig_Loanid = form.cleaned_data['Orig_Loanid'], Orig_Loanamount = form.cleaned_data['Orig_Loanamount'], Orig_Loandate = form.cleaned_data['Orig_Loandate'], Published=form.cleaned_data['Published'], SHA_256=HASH)
		a.save()
		"""
		with open('media/'+str(a.upload), 'rb') as f:
        	    for block in iter(lambda: f.read(65536), b''):
            		sha256.update(block)
		HASH = sha256.hexdigest()
		a.SHA_256 = HASH
		a.save()
		"""
                return redirect("/")
            else:
                print "error"
                print form.errors
        except:
            raise
            print "error here"
            print form.errors
            pass
            #return render(request, 'student/register.html', {'form': form})
            
    else:
        form = RegisterForm()

    return render(request, 'student/register.html', {'form': form})



