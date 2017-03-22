from django.db import models
from django.contrib.auth.models import User 
from datetime import date, datetime

class UserInfo(models.Model):
    Orig_Platform = models.CharField(max_length = 25)
    Orig_Loanid = models.CharField( max_length = 25)
    Orig_Loanamount = models.CharField( max_length = 25)
    Orig_Loandate = models.DateField( default=date.today)
    Published = models.IntegerField()
    upload = models.FileField(upload_to='uploads/')

