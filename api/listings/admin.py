from django.contrib import admin

from . import models


class ListingAdmin(admin.ModelAdmin):
    """ Custom Admin listing"""
    list_display = ["id", "title", "address", "price"]
    list_display_links = ["id", "title"]


admin.site.register(models.Listing, ListingAdmin)
