from django.contrib import admin
from .models import Route, Address, Area, City
from import_export.admin import ImportExportModelAdmin
admin.site.register(Route)
admin.site.register(Address)
@admin.register(Area)
class AreaAdmin(ImportExportModelAdmin):
    pass
@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    pass