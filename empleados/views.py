from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Empleado
from django.contrib import messages

def index(request):
    try:
        empleados = Empleado.objects.all().order_by('-fecha_contratacion')
        context = {
            'empleados': empleados
        }
        return render(request, 'empleados/index.html', context)
    except Exception as e:
        return HttpResponse(f"Error en la vista: {str(e)}")

def agregar_empleado(request):
    if request.method == 'POST':
        try:
            # Validar RFC único
            rfc = request.POST['rfc'].strip().upper()
            if Empleado.objects.filter(rfc=rfc).exists():
                return render(request, 'empleados/agregar_empleado.html', {
                    'error': 'El RFC ya está registrado en el sistema.'
                })
            
            empleado = Empleado(
                nombre=request.POST['nombre'].strip().title(),
                apellidos=request.POST['apellidos'].strip().title(),
                rfc=rfc,
                puesto=request.POST['puesto'],
                fecha_contratacion=request.POST['fecha_contratacion']
            )
            empleado.save()
            messages.success(request, '✅ Empleado agregado correctamente!')
            return redirect('index')
            
        except Exception as e:
            return render(request, 'empleados/agregar_empleado.html', {
                'error': f'❌ Error al agregar empleado: {str(e)}'
            })
    
    return render(request, 'empleados/agregar_empleado.html')

def editar_empleado(request, id_empleado):
    try:
        empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
        
        if request.method == 'POST':
            try:
                # Validar RFC único excluyendo el actual
                rfc = request.POST['rfc'].strip().upper()
                if Empleado.objects.filter(rfc=rfc).exclude(id_empleado=id_empleado).exists():
                    return render(request, 'empleados/editar_empleado.html', {
                        'empleado': empleado,
                        'error': '❌ El RFC ya está registrado por otro empleado.'
                    })
                
                empleado.nombre = request.POST['nombre'].strip().title()
                empleado.apellidos = request.POST['apellidos'].strip().title()
                empleado.rfc = rfc
                empleado.puesto = request.POST['puesto']
                empleado.fecha_contratacion = request.POST['fecha_contratacion']
                empleado.save()
                
                messages.success(request, '✅ Empleado actualizado correctamente!')
                return redirect('index')
                
            except Exception as e:
                return render(request, 'empleados/editar_empleado.html', {
                    'empleado': empleado,
                    'error': f'❌ Error al actualizar empleado: {str(e)}'
                })
        
        return render(request, 'empleados/editar_empleado.html', {'empleado': empleado})
    except Exception as e:
        return HttpResponse(f"Error al editar: {str(e)}")

def eliminar_empleado(request, id_empleado):
    try:
        empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
        
        if request.method == 'POST':
            empleado.delete()
            messages.success(request, '✅ Empleado eliminado correctamente!')
            return redirect('index')
        
        return render(request, 'empleados/eliminar_empleado.html', {'empleado': empleado})
    except Exception as e:
        return HttpResponse(f"Error al eliminar: {str(e)}")