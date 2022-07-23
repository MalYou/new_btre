from django.contrib import admin

from . import models


class ListingAdmin(admin.ModelAdmin):
    """ Custom Admin listing"""
    list_display = ["id", "title", "address", "price"]
    list_display_links = ["id", "title"]


class AttachmentAdmin(admin.ModelAdmin):
    """ Custom Admin for attachment"""
    list_display = ["is_main", "path"]
    list_display_links = ["path"]


admin.site.register(models.Listing, ListingAdmin)
admin.site.register(models.Attachment, AttachmentAdmin)
