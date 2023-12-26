from django.shortcuts import render, redirect, get_object_or_404
from .models import factura
from .forms import FacturaForm

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_facturas')
    else:
        form = FacturaForm()
    return render(request, 'crear_factura.html', {'form': form})

def ver_factura(request, pk):
    facturas = get_object_or_404(factura, pk=pk)
    return render(request, 'ver_factura.html', {'factura': facturas})

def editar_factura(request, pk):
    facturas = get_object_or_404(factura, pk=pk)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=facturas)
        if form.is_valid():
            form.save()
            return redirect('ver_factura', pk=pk)
    else:
        form = FacturaForm(instance=facturas)
    return render(request, 'editar_factura.html', {'form': form, 'factura': facturas})

def eliminar_factura(request, pk):
    facturas = get_object_or_404(factura, pk=pk)
    if request.method == 'POST':
        facturas.delete()
        return redirect('lista_facturas')
    return render(request, 'eliminar_factura.html', {'factura': facturas})

def lista_facturas(request):
    facturas = factura.objects.all()
    return render(request, 'lista_facturas.html', {'factura': facturas})

