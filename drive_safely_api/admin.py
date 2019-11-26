from django.contrib import admin

# Register your models here.

from drive_safely_api.models import Advice, Photo

admin.site.register(Advice)
admin.site.register(Photo)