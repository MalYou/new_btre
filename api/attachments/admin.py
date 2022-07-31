from django.contrib import admin

from . import models


class AttachmentAdmin(admin.ModelAdmin):
    """ Custom Admin for attachment"""
    list_display = ("id", "is_main", "path", "listing_id")
    list_display_links = ("id",)


admin.site.register(models.Attachment, AttachmentAdmin)
