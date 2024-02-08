from django.shortcuts import render, redirect, get_object_or_404
from .models import factura
from .forms import FacturaForm
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

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

def ver_pdf(request, pk):
    facturas = get_object_or_404(factura, pk=pk)
    # Suponiendo que archivoFactura es un campo FileField en tu modelo
    pdf_path = facturas.Documento_factura.path

    # Abre el archivo PDF y devuelve su contenido como una respuesta HTTP
    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')

    return response

@csrf_exempt
def verificar_facturas_pendientes(request):
    facturas_pendientes = factura.objects.filter(Pago_de_detraccion=False).values('Orden_de_trabajo')
    data = {'facturas_pendientes': list(facturas_pendientes)}
    return JsonResponse(data)

