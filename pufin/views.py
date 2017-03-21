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

@csrf_exempt
def Form(request):
    #deleteevent()
    print "signup"
    if request.method == 'POST':
        print "post signup"
        form = RegisterForm(request.POST)
        try:
            if form.is_valid():
                print form.cleaned_data
    	        if form.cleaned_data['passwd1'] != form.cleaned_data['passwd2']:
                        messages.add_message(request, messages.ERROR, 'Passwords do not match.')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                if User.objects.filter(email=form.cleaned_data['emailid']).count():
                        messages.add_message(request, messages.ERROR, 'Email already in Use')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                if UserInfo.objects.filter(pin=form.cleaned_data['pin']).count():
                        messages.add_message(request, messages.ERROR, 'Pin already taken')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                if User.objects.filter(username=form.cleaned_data['username']).count():
                        messages.add_message(request, messages.ERROR, 'Username already taken')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
                u = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['emailid'], form.cleaned_data['passwd1'] )
                ui = UserInfo()
                ui.user = u
                ui.class_of = form.cleaned_data['gradyear']
                ui.grade = form.cleaned_data['grade']
                ui.balance = 0
                ui.pin = form.cleaned_data['pin']
		ui.id = u.id
                u.first_name = form.cleaned_data['first_name']
		ui.first_name = form.cleaned_data['first_name']
                u.last_name = form.cleaned_data['last_name']
		ui.last_name = form.cleaned_data['last_name']
		ui.email = form.cleaned_data['emailid']
                u.username = form.cleaned_data['username']
                u.save()
		print u.id
                ui.save()
		#j = User.objects.get(id = 3932)
		#print j
                print "DONE"
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['passwd1'])
                login(request,user)
                print "after login in signup"
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

    return render(request, '/student/register.html', {'form': form})



