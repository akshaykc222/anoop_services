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

class Desingation(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="userDesingationCreate",on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    name = models.CharField(max_length=160,default="admin")
    phone = models.CharField(max_length=20)
    designation=models.ForeignKey(Desingation,on_delete=models.CASCADE,related_name="UserDesignation",null=True)
    created_user = models.ForeignKey('self',null=True,blank=True,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.email

class Region(models.Model):
    name=models.CharField(max_length=150)

class Role(models.Model):
    # id = models.IntegerField(db_index=True, primary_key=True)

    role_name = models.CharField(db_index=True, max_length=100)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="userRoleCreate",on_delete=models.PROTECT)
    def __str__(self):
        return self.role_name

class Business(models.Model):
    # id=models.IntegerField(primary_key=True,db_index=True)
    parent_company=models.OneToOneField("self",blank=True,on_delete=models.PROTECT,related_name="parent",null=True)
    name=models.CharField(max_length=200,db_index=True)
    address=models.TextField(max_length=200,db_index=True)
    pin_code=models.IntegerField(db_index=True)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100,db_index=True)
    city=models.CharField(max_length=100,db_index=True)
    city=models.CharField(max_length=100,db_index=True)
    tax1=models.CharField(max_length=50,db_index=True)
    tax2=models.CharField(max_length=50,db_index=True)
    # region=models.ForeignKey(Region,related_name="region",on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="userBusiness",on_delete=models.PROTECT)
    def  __str__(self):
        return self.name
    


class UserRoles(models.Model):
    
    role=ForeignKey(Role,on_delete=models.PROTECT,related_name="role",db_index=True)
    business=ForeignKey(Business,on_delete=models.PROTECT,related_name="business",db_index=True)
    user=ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name="user",db_index=True)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="userRole",on_delete=models.PROTECT,db_index=True)
    def __str__(self):
        return f'{self.role}==>{self.business}==>{self.user}'
    


    
class Categories(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="categories_created_user",on_delete=models.PROTECT,db_index=True)

    def __str__(self):
        return self.name

class SubCategories(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    category=models.ForeignKey(Categories,on_delete=models.PROTECT,related_name="category",db_index=True)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="subcategories_created_user",on_delete=models.PROTECT,db_index=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    subCategory = models.ForeignKey(SubCategories,on_delete=models.PROTECT,related_name="sub_category",db_index=True)
    name = models.CharField(max_length=150,db_index=True)
    is_product=models.BooleanField(default=False,db_index=True)
    purchase_rate = models.FloatField(null=True,blank=True,db_index=True)
    mrp = models.FloatField(db_index=True,null=True,blank=True)
    sales_percentage = models.FloatField(db_index=True,null=True,blank=True)
    sales_rate = models.FloatField(db_index=True,null=True,blank=True)
    tax_rate = models.FloatField(db_index=True,null=True,blank=True)
    duration = models.FloatField(db_index=True,blank=True,null=True)
    expiry_date = models.DateField(db_index=True,null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)

    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="product_created_user",on_delete=models.PROTECT,db_index=True)


class ProductImages(models.Model):
    product = models.ForeignKey(Products,related_name="prodcut_image",on_delete=models.PROTECT)
    image = models.ImageField()
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="product_image_created_user",on_delete=models.PROTECT,db_index=True)


    def __str__(self):
        return self.name
    
class Customers(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    email = models.EmailField(_('email address'),),
    blood = models.CharField(null=True,max_length=20)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode =models.IntegerField(default=0)
    address = models.TextField(max_length=250)
    insurance_comapny = models.CharField(max_length=150)
    insurance_expiry = models.DateField()
    insurance_num = models.CharField(db_index=True,max_length=50)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="customerCreatedUser",on_delete=models.PROTECT,db_index=True)


    def __str__(self):
        return self.name

class Appointments(models.Model):
    customer = models.ForeignKey(Customers,related_name="customer",on_delete=models.PROTECT)
    booking_date =models.DateTimeField()
    refferd_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="refferdBy",on_delete=models.PROTECT,db_index=True)
    proposed_fee = models.FloatField()
    customer_fee = models.FloatField()
    amount_paid = models.FloatField()
    due_amount = models.FloatField()
    initial_consultant = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="initial_cosultant",on_delete=models.PROTECT,db_index=True)
    main_consultant = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="main_cosultant",on_delete=models.PROTECT,db_index=True)
   
    reminder_date = models.DateField()
    notes = models.TextField()
    status= models.CharField(max_length=3,default="P")
    
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="appointmentCreatedUser",on_delete=models.PROTECT,db_index=True)


    def __str__(self):
        return self.customer



class Tax(models.Model):
    name = models.CharField(max_length=100)
    short_name =models.CharField(max_length=100)
    tax_percentage= models.FloatField(default=0.00)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="taxCreatedUser",on_delete=models.PROTECT,db_index=True)


    def __str__(self):
        return self.name

class Unit(models.Model):
    unit_name=models.CharField(max_length=20)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="unitCreatedUser",on_delete=models.PROTECT,db_index=True)


    def __str__(self):
        return self.unit_name

class pages(models.Model):
    page_name=models.CharField(max_length=100,db_index=True)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="pageCreated",on_delete=models.PROTECT,db_index=True)


    def __str__(self):
        return self.page_name


    
class RolePermissions(models.Model):
    role=models.ForeignKey(Role,related_name="roleMap",on_delete=models.PROTECT,db_index=True)
    page_name=models.ForeignKey(pages,related_name="pages",on_delete=models.PROTECT,db_index=True)
    read=models.BooleanField(default=False,db_index=True)
    create=models.BooleanField(default=False,db_index=True)
    delete=models.BooleanField(default=False,db_index=True)
    update=models.BooleanField(default=False,db_index=True)
    created_date=models.DateTimeField(auto_now_add=True,db_index=True)
    created_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="rolePermission",on_delete=models.PROTECT,db_index=True)



class DefaultBusiness(models.Model):
    defualt_business=models.ForeignKey(Business,related_name="defualtBusiness",on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="defaultBusUser",on_delete=models.CASCADE)
