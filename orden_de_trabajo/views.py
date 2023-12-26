from django.shortcuts import render, redirect, get_object_or_404
from .models import Orden_trabajo
from .forms import OrdenTrabajoForm

# Create your views here.
def crear_orden_trabajo(request):
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ordenes_trabajo')
    else:
        form = OrdenTrabajoForm()
    return render(request, 'crear_orden_trabajo.html', {'form': form})

def ver_orden_trabajo(request, pk):
    orden_trabajo = get_object_or_404(Orden_trabajo, pk=pk)
    return render(request, 'ver_orden_trabajo.html', {'orden_trabajo': orden_trabajo})

def editar_orden_trabajo(request, pk):
    orden_trabajo = get_object_or_404(Orden_trabajo, pk=pk)
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST, instance=orden_trabajo)
        if form.is_valid():
            form.save()
            return redirect('ver_orden_trabajo', pk=pk)
    else:
        form = OrdenTrabajoForm(instance=orden_trabajo)
    return render(request, 'editar_orden_trabajo.html', {'form': form, 'orden_trabajo': orden_trabajo})

def eliminar_orden_trabajo(request, pk):
    orden_trabajo = get_object_or_404(Orden_trabajo, pk=pk)
    if request.method == 'POST':
        orden_trabajo.delete()
        return redirect('lista_ordenes_trabajo')
    return render(request, 'eliminar_orden_trabajo.html', {'orden_trabajo': orden_trabajo})

def lista_ordenes_trabajo(request):
    ordenes_trabajo = Orden_trabajo.objects.all()
    return render(request, 'lista_ordenes_trabajo.html', {'ordenes_trabajo': ordenes_trabajo})
