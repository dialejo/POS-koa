# Register your models here.

from django.contrib import admin
from .models.user import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'name')
    search_fields = ('username', 'email', 'name')
    

admin.site.register(User)