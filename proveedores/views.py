import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import proveedorForm

def crear_proveedor(request):
    if request.method == 'POST':
        form = proveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = proveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})

def ver_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.nombre_archivo = os.path.basename(proveedor.DocumentacionLegal.name)
    return render(request, 'ver_proveedor.html', {'proveedor': proveedor})

def editar_proveedor(request, pk):
    proveedores = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = proveedorForm(request.POST, instance=proveedores)
        if form.is_valid():
            form.save()
            return redirect('ver_proveedor', pk=pk)
    else:
        form = proveedorForm(instance=proveedores)
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedores})

def eliminar_proveedor(request, pk):
    proveedores = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedores.delete()
        return redirect('lista_proveedores')
    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedores})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    for proveedor in proveedores:
        proveedor.nombre_archivo = os.path.basename(proveedor.DocumentacionLegal.name)
    return render(request, 'lista_proveedores.html', {'proveedor': proveedores})