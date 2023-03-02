from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Profile, UserAddress


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_user_profile_address(instance, created, **kwargs):
    if created:
        usr_addr = UserAddress.objects.create()
        instance.address = usr_addr
        instance.save()
