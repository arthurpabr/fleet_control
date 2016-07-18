from datetime import date
from django.contrib import admin
from .models import Driver, Manufacturer, Vehicle, UseControl, Manager

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    #list_display = ('name', 'licence_plate', 'manufacture_year', 'is_activate')
    list_display = ('name', 'licence_plate', 'year_format', 'is_activate')
    list_display_links = ('name', 'licence_plate')
    list_per_page = 3
    search_fields = ('name', 'description')
    list_filter = ('is_activate',)

    def year_format(self, instance):
        return date.strftime(instance.manufacture_year,"%Y")
    year_format.short_description = 'Ano de fabricação'

@admin.register(UseControl)
class UseControlAdmin(admin.ModelAdmin):
    pass

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass
