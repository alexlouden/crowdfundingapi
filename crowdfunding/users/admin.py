from django.contrib import admin
from .models import CustomUser, SupporterProfile, OwnerProfile

admin.site.register(CustomUser)
admin.site.register(SupporterProfile)
admin.site.register(OwnerProfile)
