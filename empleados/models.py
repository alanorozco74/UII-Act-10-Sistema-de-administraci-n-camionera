from django.db import models

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13, unique=True)
    puesto = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    
    class Meta:
        db_table = 'empleados'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.puesto}"