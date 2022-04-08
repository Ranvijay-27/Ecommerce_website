from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    slug = models.CharField(max_length = 150,null = False,blank=False)
    name = models.CharField(max_length = 150,null = False,blank=False)
    image = models.ImageField(upload_to = "img/",null = True,blank = True) 
    status = models.BooleanField(default=False,help_text="0= default ,1=Hidden")
    trending = models.BooleanField(default=False,help_text="0= default ,1=Trending")
    weight = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length = 150,null = False,blank=False)
    name = models.CharField(max_length = 150,null = False,blank=False)
    product_image = models.ImageField(upload_to = "img/",null = True,blank = True) 
    status = models.BooleanField(default=False,help_text="0= default ,1=Hidden")
    trending = models.BooleanField(default=False,help_text="0= default ,1=Trending")
    quantity = models.IntegerField(null = False,blank=False)
    price = models.IntegerField(null = False,blank=False)
    color = models.CharField(max_length = 150,null = False,blank=False)
    def __str__(self):
        return self.name

        

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null = False,blank=False)

class ProductReview(models.Model):
    name = models.CharField(max_length = 150,null = False,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.IntegerField()
    review_text = models.TextField()
    review_rating = models.CharField(max_length=150) 
class PopUp(models.Model):
  
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=150)     
    
class Wichlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)