from django.shortcuts import render, redirect, get_object_or_404
from .models import unidades
from .forms import unidadesForm

# Create your views here.
def crear_unidad(request):
    if request.method == 'POST':
        form = unidadesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_unidades')
    else:
        form = unidadesForm()
    return render(request, 'crear_unidad.html', {'form': form})

def ver_unidad(request, pk):
    unidad = get_object_or_404(unidades, pk=pk)
    return render(request, 'ver_unidad.html', {'unidad': unidad})

def editar_unidad(request, pk):
    unidad_obj = get_object_or_404(unidades, pk=pk)
    if request.method == 'POST':
        form = unidadesForm(request.POST, instance=unidad_obj)
        if form.is_valid():
            form.save()
            return redirect('ver_unidad', pk=pk)
    else:
        form = unidadesForm(instance=unidad_obj)
    return render(request, "editar_unidad.html", {'form': form, 'unidad': unidad_obj})

def eliminar_unidad(request, pk):
    unidad_obj = get_object_or_404(unidades, pk=pk)
    if request.method == 'POST':
        unidad_obj.delete()
        return redirect('lista_unidades')
    return render(request, 'eliminar_unidad.html', {'unidad': unidad_obj})

def lista_unidades(request):
    unidad = unidades.objects.all()
    return render(request, 'lista_unidades.html', {'unidad': unidad})