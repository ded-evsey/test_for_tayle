from django.contrib import admin
from catalog.models import Characteristic, Product, Section
# Register your models here.


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'id']
    list_filter = ['name', 'value']
    search_fields = ['name', 'value']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'id']
    list_filter = ['characteristics', 'sections']
    search_fields = ['name', 'sections']


class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'id']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Section, SectionAdmin)
