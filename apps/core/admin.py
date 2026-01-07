from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SiteInfo


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "phone_number", "email")   
    search_fields = ("title", "phone_number", "email")  
