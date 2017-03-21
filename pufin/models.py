from django.db import models
from django.contrib.auth.models import User 
from datetime import date, datetime

class UserInfo(models.Model):
    #user = models.OneToOneField(User, related_name='user_infos')
    #class_of = models.IntegerField()
    #username = user.username
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 30)
    #email = models.EmailField(max_length = 100) 
    #Staff = user.is_staff
    #pub_date = models.DateField(default=date.today)
    #grade = models.IntegerField()
    #balance = models.DecimalField(max_digits=6, decimal_places=2)
    #pin = models.DecimalField(max_digits=4, decimal_places=0)
    #first_name = models.CharField(max_length = 25)
    #id = models.IntegerField(primary_key = True)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
