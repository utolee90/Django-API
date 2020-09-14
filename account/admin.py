from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from .models import User

#Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number']
    list_display_links = ['username', 'email', 'phone_number']
    
