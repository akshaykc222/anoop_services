import datetime
from django import db
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.fields import FloatField
from django.db.models.fields.related import ForeignKey
from rest_framework_simplejwt.tokens import RefreshToken
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from fresh_django import settings
from datetime import date


    
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    name = models.CharField(max_length=160,default="admin")
    phone = models.CharField(max_length=20)
    
    created_user = models.ForeignKey('self',null=True,blank=True,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.email



class Business(models.Model):
    # id=models.IntegerField(primary_key=True,db_index=True)
    # parent_company=models.OneToOneField("self",blank=True,on_delete=models.PROTECT,related_name="parent",null=True)
    name=models.CharField(max_length=200,db_index=True)
    address=models.TextField(max_length=200,db_index=True)
    image=models.CharField(max_length=300)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="userBusiness",on_delete=models.PROTECT)
    # pin_code=models.IntegerField(db_index=True)
    # country=models.CharField(max_length=100)
    # state=models.CharField(max_length=100,db_index=True)
    # city=models.CharField(max_length=100,db_index=True)
    # city=models.CharField(max_length=100,db_index=True)
    # tax1=models.CharField(max_length=50,db_index=True)
    # tax2=models.CharField(max_length=50,db_index=True)
    # region=models.ForeignKey(Region,related_name="region",on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
   
    def  __str__(self):
        return self.name
    

class TimeSlots(models.Model):
    slot=models.CharField(max_length=150)



class Appointments(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="customer",on_delete=models.PROTECT)
    booking_date =models.DateTimeField()
    business = models.ForeignKey(Business,related_name="main_cosultant",on_delete=models.PROTECT,db_index=True)
    # business = models.ForeignKey(Business,related_name="customerbb",on_delete=models.PROTECT)
    # refferd_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="refferdBy",on_delete=models.PROTECT,db_index=True)
    # proposedpy_fee = models.FloatField()
    # customer_fee = models.FloatField()
    # amount_paid = models.FloatField()
    # due_amount = models.FloatField()
    # initial_consultant = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="initial_cosultant",on_delete=models.PROTECT,db_index=True)
    # main_consultant = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="main_cosultant",on_delete=models.PROTECT,db_index=True)
    slot = models.ForeignKey(TimeSlots,related_name="timeslot",on_delete=models.PROTECT)
    # reminder_date = models.DateField()
    # notes = models.TextField()
    status= models.CharField(max_length=3,default="P")


    created_date=models.DateField()
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="appointmentCrddeatedUser",on_delete=models.PROTECT,db_index=True)


    


class Feedback(models.Model):
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="appointmentCreatedUser",on_delete=models.PROTECT,db_index=True)
    shop=models.ForeignKey(Business,related_name="bus",on_delete=models.CASCADE)
    rate=models.FloatField()
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="owner",on_delete=models.PROTECT)


class reports(models.Model):
    reports=models.URLField('https://admin.uniongates.com/Report.html')