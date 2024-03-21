from django.contrib import admin
from django import forms
from .models import Equipment, User_Equipment, Brand, Type, Supplier


admin.site.site_header = 'Administracion de Inventario'
admin.site.site_title = 'Administracion de Inventario'
admin.site.index_title = 'Administracion de Inventario'

# admin.site.register(Equipment)
# admin.site.register(User_Equipment)
admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Supplier)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'brand', 'type', 'date_created')
    search_fields = ('reference','')
    list_filter = ('type', 'date_created')
    list_per_page = 20


@admin.register(User_Equipment)
class UserEquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'equipment', 'user', 'assignment_date')
    list_filter = ('assignment_date', 'user')



