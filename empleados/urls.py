from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('editar/<int:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<int:id_empleado>/', views.eliminar_empleado, name='eliminar_empleado'),
]