from datetime import datetime

import stripe
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

MEMBERSHIP_CHOICES = (
    ('Enterprise', 'ent'),
    ('Professional', 'pro'),
    ('Free', 'free')
)


class Video(models.Model):
    thumbnail = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    video = models.FileField(upload_to='video')
    price = models.IntegerField()
    porm = models.ManyToManyField(User, related_name='porm')
    name = models.CharField(max_length=30)
    descreption = models.TextField(max_length=30, null=True)


class Friend(models.Model):
    users = models.ManyToManyField(User, related_name='users')
    current_user = models.ManyToManyField(Video, related_name='owners')

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)
