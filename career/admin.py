from django.contrib import admin

from .models import (Coordinate, DumpTruck, DumpTruckMineral, Mineral,
                     Warehouse, WarehouseMineral)


class DumpTruckMineralInLine(admin.TabularInline):
    model = DumpTruckMineral
    extra = 0


class DumpTruckAdmin(admin.ModelAdmin):
    inlines = (DumpTruckMineralInLine, )
    list_display = ('number', 'model')


class DumpTruckMineralAdmin(admin.ModelAdmin):
    list_display = ('weight', 'dump_truck', 'mineral')


class WarehouseMineralInLine(admin.TabularInline):
    model = WarehouseMineral
    extra = 0


class WarehouseAdmin(admin.ModelAdmin):
    inlines = (WarehouseMineralInLine, )
    filter_horizontal = ('polygon_coord',)
    list_display = ('title',)


class WarehouseMineralAdmin(admin.ModelAdmin):
    list_display = ('weight', 'warehouse', 'mineral')


class MineralAdmin(admin.ModelAdmin):
    list_display = ('iron_content', 'silicon_content')


class CoordinateAdmin(admin.ModelAdmin):
    list_display = ('x_coordinate', 'y_coordinate')


admin.site.register(DumpTruck, DumpTruckAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Mineral, MineralAdmin)
admin.site.register(Coordinate, CoordinateAdmin)
admin.site.register(WarehouseMineral, WarehouseMineralAdmin)
admin.site.register(DumpTruckMineral, DumpTruckMineralAdmin)
