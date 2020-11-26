from .models import Route, Address, RouteBestPath
from django.contrib.gis import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget


admin.site.register(Route)
admin.site.register(RouteBestPath)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
