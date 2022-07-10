from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CarBrand, CarModel, Engine


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded', 'headquaters', 'get_html_logo')
    search_fields = ('name',)

    def get_html_logo(self, object):
        if object.logo:
            return mark_safe(f'<img src="{object.logo.url}" width=50>') # Не отображает почему-то
    get_html_logo.short_description = 'Logotype'


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'name', 'made_in', 'model_years', 'body_style',
             'clasification', 'engine',# 'engine_displacement', 'engine_fuel_type'
        )
    search_fields = ('name', 'model_years', 'body_style', 'clasification')
    filter_horizontal = ('engine',)
    raw_id_fields = ('brand', 'engine')

    def brand_name(self, obj):
        return obj.brand.name

    brand_name.admin_order_field = 'brand__name'

    # def engine_displacement(self, obj):
    #     return obj.engine.displacement

    # def engine_fuel_type(self, obj):
    #     return obj.engine.fuel_type
    # Из m2m не вытягиваються данные

    def engine(self, obj): # car_catalog.Engine.None в результате, почему не выяснилось
        return obj.engine


class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'made_in', 'model_years', 'displacement',
            'fuel_type', 'torque', 'power', 'fuel_consumption'
        )
    search_fields = ('name', 'displacement', 'fuel_type')


admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Engine, EngineAdmin)
