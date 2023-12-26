from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import notificacion
from .forms import NotificacionesForm

def crear_notificaciones(request):
    if request.method == 'POST':
        form = NotificacionesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_notificaciones')
    else:
        form = NotificacionesForm()
    return render(request, 'crear_notificaciones.html', {'form': form})

def ver_notificaciones(request, pk):
    notificaciones = get_object_or_404(notificacion, pk=pk)
    return render(request, 'ver_notificaciones.html', {'notificacion': notificaciones})

def editar_notificaciones(request, pk):
    notificaciones = get_object_or_404(notificacion, pk=pk)
    if request.method == 'POST':
        form = NotificacionesForm(request.POST, instance=notificaciones)
        if form.is_valid():
            form.save()
            return redirect('ver_notificaciones', pk=pk)
    else:
        form = NotificacionesForm(instance=notificaciones)
    return render(request, 'editar_notificaciones.html', {'form': form, 'notificacion': notificaciones})

def eliminar_notificaciones(request, pk):
    notificaciones = get_object_or_404(notificacion, pk=pk)
    if request.method == 'POST':
        notificaciones.delete()
        return redirect('lista_notificaciones')
    return render(request, 'eliminar_notificaciones.html', {'notificacion': notificaciones})

def lista_notificaciones(request):
    notificaciones = notificacion.objects.all()
    return render(request, 'lista_notificaciones.html', {'notificacion': notificaciones})