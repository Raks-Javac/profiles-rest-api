from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
# This registers your userprofile model in the django admin
