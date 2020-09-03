from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

    def is_supporter(self):
        """ is the user a supporter """
        return self.supporter_pledges.filter(anonymous=False).count() > 0
    is_supporter.boolean = True

    def is_owner(self):
        """ is the user an owner """
        return self.shelters.all().count() > 0
    is_owner.boolean = True

    def get_shelter(self):
        return self.shelters.all()


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name = 'profile'
    )
    bio = models.TextField(blank=True)
    petlikes = models.ManyToManyField(
        "projects.PetTag",
        related_name = "liked_by",
        related_query_name = "pet"
    )

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
