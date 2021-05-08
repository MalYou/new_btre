from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """ Custom Admin User """
    list_display = ['id', 'email', 'first_name', 'last_name', 'phone', 'is_staff', 'is_customer']
    list_display_links = ['id', 'email']


admin.site.register(User, UserAdmin)
