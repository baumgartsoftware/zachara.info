from django.db import models
from django.contrib.auth.models import User

from main.utils import user_dir_path


class UserAddress(models.Model):
    address = models.CharField(max_length=255, blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'Location  {self.pk}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_dir_path, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.OneToOneField(UserAddress, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username.__str__() + 'Profile'
