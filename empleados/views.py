from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleados
from .forms import EmpleadosForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def crear_empleados(request):
    if request.method == 'POST':
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadosForm()
    return render(request, 'crear_empleados.html', {'form': form})

@login_required
def ver_empleados(request, pk):
    empleados = get_object_or_404(Empleados, pk=pk)
    return render(request, 'ver_empleados.html', {'empleados': empleados})

@login_required
def editar_empleados(request, pk):
    empleados = get_object_or_404(Empleados, pk=pk)
    if request.method == 'POST':
        form = EmpleadosForm(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            return redirect('ver_empleados', pk=pk)
    else:
        form = EmpleadosForm(instance=empleados)
    return render(request, 'editar_empleados.html', {'form': form, 'empleados': empleados})

@login_required
def eliminar_empleados(request, pk):
    empleados = get_object_or_404(Empleados, pk=pk)
    if request.method == 'POST':
        empleados.delete()
        return redirect('lista_empleados')
    return render(request, 'eliminar_empleados.html', {'empleados': empleados})

@login_required
def lista_empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'lista_empleados.html', {'empleados': empleados})
