from django.contrib.auth import get_user_model
from django.db import models


class Shelter(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    charityregister = models.IntegerField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='shelters'
    )

    def __str__(self):
        return self.name

class PetTag(models.Model):
    petspecies = models.CharField(max_length=200)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    species = models.ManyToManyField(
        PetTag,
        related_name = "pets",
        related_query_name = "pet"
    )
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name='projects', null=True)

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )