from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Preferences


@receiver(post_save, sender=User)
def create_preferences(sender, instance, created, **kwargs):
    if created:
        Preferences.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_preferences(sender, instance, **kwargs):
    instance.preferences.save()
