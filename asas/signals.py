from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Asas

@receiver(post_save, sender=User)
def create_Asas(sender, instance, created, **kwargs):
    if created:
        Asas.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_Asas(sender, instance,  **kwargs):
    instance.Profile.save()
