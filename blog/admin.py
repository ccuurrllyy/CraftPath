from django.contrib import admin
from mapwidgets.widgets import GooglePointFieldWidget
from django.forms import widgets
from django.contrib.gis.db import models
from .models import Route, Address, Area, City
from import_export.admin import ImportExportModelAdmin
from django import forms





from django.contrib.gis import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget


admin.site.register(Route)


@admin.register(Area)
class AreaAdmin(ImportExportModelAdmin):
    pass
@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }