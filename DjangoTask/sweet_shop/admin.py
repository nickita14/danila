from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget

from . import models


class ProductResource(resources.ModelResource):
    categories = fields.Field(column_name='categories', attribute='categories',
                              widget=ManyToManyWidget(models.Category, field='name'))

    class Meta:
        model = models.Product
        fields = (
            'name', 'price', 'categories', 'composition', 'packaging', 'energy_value', 'manufacturer',
            'shelf_life',
            'certificates')
        exclude = ('slug', )


class ProductAdmin(ImportExportActionModelAdmin):
    resources_class = ProductResource
    list_display = ('id', 'name', 'photo', 'price', 'time_create')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'photo', 'price')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
#     prepopulated_fields = {'slug':('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)
