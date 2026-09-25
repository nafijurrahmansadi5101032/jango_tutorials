from django.contrib import admin
from .models import profile

@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


