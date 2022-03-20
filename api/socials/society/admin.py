from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'avatar', 'status', 'publicity']


admin.site.register(User, UserAdmin)
