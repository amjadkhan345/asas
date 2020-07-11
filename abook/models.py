from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, CharField
from django.db.models.signals import post_save

#from products.models import Product

import stripe
from django.conf import settings
#from book.book import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

# from . import models
# from .models import Order
from asas.models import Book


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ebooks = models.ManyToManyField(Book, blank=True)
    image = models.ImageField(upload_to='pro', default=True)
    address = models.CharField(max_length=122, null=True)
    contry = models.CharField(max_length=32)
    mobil = models.CharField(max_length=15)

    # def __init__(self, *args, **kwargs):
    # super().__init__(*args, **kwargs)
    # self.User = None

    def __set__(self):
        return self.mobil

   # def post_save_profile_create(sender, instance, created, *args, **kwargs):
      #  user_profile, created = Profile.objects.get_or_create(user=instance)



   # post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)






# class Sher(models.Model):
# User =models.OneToOneField(User, null=True, on_delete=models.CASCADE)
# title = models.CharField(max_length=150)
# image =models.ImageField(upload_to='pro', null=True, blank=True)
# objects = models.manager
