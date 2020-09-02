from django.contrib import admin
from .models import Project, Pledge, PetTag, Shelter

# Register your models here.
admin.site.register(Shelter)
admin.site.register(PetTag)
admin.site.register(Project)
admin.site.register(Pledge)
