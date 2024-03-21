from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name='nombre')
    description = models.TextField(verbose_name='descripcion', blank=True)
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='nombre')
    description = models.TextField(verbose_name='descripcion', blank=True)
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=150, verbose_name='nombre')
    description = models.TextField(verbose_name='descripcion')
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    def __str__(self):
        return self.name

class Equipment(models.Model):
    # id, referencia,marcar y tipo. Filtros por tipo y buscador por referencia
    reference = models.CharField(max_length=150, verbose_name='referencia')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name='marca')
    processor = models.CharField(max_length=150, verbose_name='procesador')
    memory = models.IntegerField(default=0, help_text="Gigabytes", verbose_name='memoria')
    disk = models.IntegerField(default=0, help_text="Gigabytes", verbose_name='disco')
    type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name='tipo')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='proveedor')
    rental_start_date = models.DateField(null=True, blank=True, verbose_name='fecha inicio de alquiler')
    rental_end_date = models.DateField(null=True, blank=True , verbose_name='fecha final de alquiler')

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return self.reference


class User_Equipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuario')
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, verbose_name='equipo', limit_choices_to={'user_equipment__isnull': True}, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')
    assignment_date = models.DateField(verbose_name='fecha de asignacion')
    delivery_date = models.DateField(verbose_name='fecha de entrega')
    class Meta:
        verbose_name = 'EquipoUsuario'
        verbose_name_plural = 'EquipoUsuario'
    def __str__(self):
        return self.equipment.reference


