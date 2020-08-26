from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_supporter = models.BooleanField('supporter status', default='False')
    is_owner = models.BooleanField('owner status', default='False')

    def __str__(self):
        return self.username

class SupporterProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        primary_key=True,
        related_name='supporter'
    )
    bio = models.TextField()

class OwnerProfile(models.Model):
    user = models.OneToOneField(
    CustomUser, 
    on_delete=models.CASCADE, 
    primary_key=True,
    related_name='owner'
    )
    shelterid = models.TextField()