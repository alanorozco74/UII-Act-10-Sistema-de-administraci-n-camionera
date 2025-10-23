from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'apellidos', 'rfc', 'puesto', 'fecha_contratacion')
    search_fields = ('nombre', 'apellidos', 'rfc')
    list_filter = ('puesto', 'fecha_contratacion')