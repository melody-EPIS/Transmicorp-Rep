from tkinter import Canvas
from django.shortcuts import render, redirect, get_object_or_404
from .models import inventario
from .forms import inventarioForm
from django.http import HttpResponse
from django.template.loader import get_template


def crear_inventario(request):
    if request.method == 'POST':
        form = inventarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_inventario')
    else:
        form = inventarioForm()
    return render(request, 'crear_inventario.html', {'form': form})

def ver_inventario(request, pk):
    inventarios = get_object_or_404(inventario, pk=pk)
    return render(request, 'ver_inventario.html', {'inventario': inventarios})

def editar_inventario(request, pk):
    inventarios = get_object_or_404(inventario, pk=pk)
    if request.method == 'POST':
        form = inventarioForm(request.POST, instance=inventarios)
        if form.is_valid():
            form.save()
            return redirect('ver_inventario', pk=pk)
    else:
        form = inventarioForm(instance=inventarios)
    return render(request, 'editar_inventario.html', {'form': form, 'inventario': inventarios})

def eliminar_inventario(request, pk):
    inventarios = get_object_or_404(inventario, pk=pk)
    if request.method == 'POST':
        inventarios.delete()
        return redirect('lista_inventario')
    return render(request, 'eliminar_inventario.html', {'inventario': inventarios})

def lista_inventario(request):
    inventarios = inventario.objects.all()
    return render(request, 'lista_inventario.html', {'inventario': inventarios})

def generar_pdf(request, pk):
    inventarios = get_object_or_404(inventario, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="inventario_{pk}.pdf"'
    p = Canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, 'Detalles del Item en el Inventario')
    p.drawString(100, 730, f'Id inventario: {inventarios.Id_Inventario}')
    p.drawString(100, 710, f'Nombre ítem: {inventarios.NombreItem}')
    p.drawString(100, 690, f'Fecha de ingreso: {inventarios.FechaIngreso}')
    p.drawString(100, 670, f'Cantidad: {inventarios.Cantidad}')
    p.drawString(100, 650, f'Número de registro: {inventarios.NumeroRegistro}')
    p.drawString(100, 630, f'Descripción: {inventarios.Descripcion}')
    p.drawString(100, 610, f'Tiempo de Vida: {inventarios.TiempoVida}')
    p.drawString(100, 590, f'Ambiente: {inventarios.Ambiente}')
    p.drawString(100, 570, f'Estado: {inventarios.Estado}')

    p.showPage()
    p.save()

    return response


