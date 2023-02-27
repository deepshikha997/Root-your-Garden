from cProfile import Profile
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from account.models import *



# Create your models here.
class Category(models.Model):
     name_cat=models.CharField(max_length=25)
     image_cat=models.ImageField(upload_to="media")
     desc_cat=models.TextField()
     updated_on=models.DateTimeField(auto_now=True)
     def __str__(self):
       return self.name_cat

class Nursery(models.Model):
     usr=models.ForeignKey(User,on_delete=models.CASCADE)
     name_nur=models.CharField(max_length=25)
     image_nur=models.ImageField(upload_to="media")
     cate=models.ForeignKey(Category,default=1,on_delete=models.CASCADE)
     desc_nur=models.TextField()
     servicecharge=models.IntegerField()
     updated_on=models.DateTimeField(auto_now=True)
     def __str__(self):
       return self.name_nur

class Service(models.Model):
    nur=models.ForeignKey(Nursery,on_delete=models.CASCADE)
    name_ser=models.CharField(max_length=25)
    desc_ser=models.TextField()
    
    price_ser=models.IntegerField()
    img_ser=models.ImageField(upload_to="media")
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.name_ser

class cart(models.Model): 
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    status=models.BooleanField(default=False)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    update_on=models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
      return self.usr.username
    
class nur_prof(models.Model):
  usr=models.ForeignKey(User,on_delete=models.CASCADE)
  service=models.ForeignKey(Service,on_delete=models.CASCADE)
  phone=models.PositiveBigIntegerField()
  add=models.CharField(max_length=500)
  maping=models.CharField(max_length=500)
  img1=models.ImageField(upload_to="pics")
  added_on=models.DateTimeField(auto_now_add=True,null=True)
  update_on=models.DateTimeField(auto_now=True,null=True)
  def __str__(self):
      return self.usr.username
    

# class Pamplate(models.Model):
#     nameofguide=models.CharField(max_length=25)
#     pamplate=models.FileField(upload_to="media/pamplate")
#     update_on=models.DateTimeField(auto_now=True,null=True)
#     desc_pamplate=models.TextField()

#     def __str__(self):
#       return self.nameofguide

class Order(models.Model):
    cust_id = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=250)
    product_ids = models.CharField(max_length=250)
    invoice_id = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    processed_on = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.cust_id.username

class contact(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    msg= models.TextField() 
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.usr.username

class feedback(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    prf=models.ForeignKey(profile, on_delete=models.CASCADE)
    # rest=models.ForeignKey(restprofile,on_delete=models.CASCADE)
    rating=models.CharField(max_length=250)
    msg=models.TextField()
    added_on=models.DateTimeField(auto_now=True,null=True)
    def _str_(self):
        return self.user.username

class billingdetails(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    state=models.TextField()
    city=models.TextField()
    street=models.TextField()
    ph_pro=models.BigIntegerField()
    det=models.TextField(max_length=80)
    def _str_(self):
        return self.usr.username

# class tips(models.Models):
#   pass
class tips(models.Model):
  Tips=models.TextField()
  plant=models.CharField(max_length=50)
  more_info=models.CharField(max_length=50,default=None)
  added_on=models.DateTimeField(auto_now=True,null=True)