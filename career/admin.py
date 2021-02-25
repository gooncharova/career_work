from django.contrib import admin

from .models import DumpTruck, Mineral


class DumpTruckAdmin(admin.ModelAdmin):
    list_display = ('number', 'model')


class MineralAdmin(admin.ModelAdmin):
    list_display = ('weight',)


admin.site.register(DumpTruck, DumpTruckAdmin)
admin.site.register(Mineral, MineralAdmin)
