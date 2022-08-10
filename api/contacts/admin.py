from django.contrib import admin

from .models import Contact


class ContactsAdmin(admin.ModelAdmin):
    """
        Admin model for contacts objects
    """

    list_display = ('id', 'message', 'customer',)


admin.site.register(Contact, ContactsAdmin)
