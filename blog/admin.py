from .models import Route, Address, RouteBestPath, RouteBestPathLocation
from django.contrib.gis import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget


admin.site.register(Route)
admin.site.register(RouteBestPathLocation)



@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


class AuthorInline(admin.TabularInline):
    model = RouteBestPathLocation


@admin.register(RouteBestPath)
class RouteBestPath(admin.ModelAdmin):
    inlines = [
        AuthorInline,
    ]
