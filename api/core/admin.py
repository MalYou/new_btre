from django.contrib import admin

from core import models


class CountryAdmin(admin.ModelAdmin):
    """ Custom Admin for countries"""
    list_display = ("name", "code")
    list_display_links = ("name",)


class StateAdmin(admin.ModelAdmin):
    """ Custom Admin for states"""
    list_display = ("name", "code", "country")
    list_display_links = ("name",)


class CityAdmin(admin.ModelAdmin):
    """ Custom Admin for cities"""
    list_display = ("name", "code", "state")
    list_display_links = ("name",)

class AddressAdmin(admin.ModelAdmin):
    """ Custom Admin for countries"""
    list_display = ("zipcode", "street", "city")
    list_display_links = ("zipcode",)

admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.State, StateAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Address, AddressAdmin)
