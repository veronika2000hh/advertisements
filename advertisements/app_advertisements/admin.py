from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    pass
admin.site.register(Advertisement, AdvertisementAdmin)