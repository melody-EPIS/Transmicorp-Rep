from django.shortcuts import render, redirect, get_object_or_404
from .models import gastos
from .forms import GastosForm
from facturas.models import factura
from facturas.forms import FacturaForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.db.models import Sum

def crear_gasto(request):
    if request.method == 'POST':
        form = GastosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_gasto')
    else:
        form = GastosForm()
    return render(request, 'crear_gasto.html', {'form': form})

def ver_gasto(request, pk):
    gasto = get_object_or_404(gastos, pk=pk)
    return render(request, 'ver_gasto.html', {'gasto': gasto})

def editar_gasto(request, pk):
    gasto = get_object_or_404(gastos, pk=pk)
    if request.method == 'POST':
        form = GastosForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('ver_gasto', pk=pk)
    else:
        form = GastosForm(instance=gasto)
    return render(request, 'editar_gasto.html', {'form': form, 'gasto': gasto})

def eliminar_gasto(request, pk):
    gasto = get_object_or_404(gastos, pk=pk)
    if request.method == 'POST':
        gasto.delete()
        return redirect('lista_gasto')
    return render(request, 'eliminar_gasto.html', {'gasto': gasto})

def lista_gasto(request):
    gasto = gastos.objects.all()
    return render(request, 'lista_gasto.html', {'gasto': gasto})

def ver_informes_contables(request):
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fechaInicio')
        fecha_fin = request.POST.get('fechaFin')
        tipo_consulta = request.POST.get('tipoConsulta')

        if tipo_consulta == 'consultarGastos':
            datos_gastos = gastos.objects.filter(Fecha_boleta__range=[fecha_inicio, fecha_fin])
            total_gastos = datos_gastos.aggregate(Sum('Monto_gastado'))['Monto_gastado__sum']

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="informe_contable_gastos.pdf"'

            buffer = BytesIO()
            p = canvas.Canvas(buffer)

            # Estilos y formato para gastos
            p.setFont("Helvetica", 12)

            # Título para GASTOS centrado
            ancho_pagina, _ = p._pagesize
            ancho_titulo = p.stringWidth("INFORMES CONTABLES GENERALES", "Helvetica", 12)
            x_titulo = (ancho_pagina - ancho_titulo) / 2
            p.drawString(x_titulo, 800, "INFORMES CONTABLES GENERALES")
            
            # Título específico para GASTOS centrado
            ancho_titulo_gastos = p.stringWidth("GASTOS", "Helvetica", 12)
            x_titulo_gastos = (ancho_pagina - ancho_titulo_gastos) / 2
            p.drawString(x_titulo_gastos, 780, "GASTOS")



            # Encabezados de la tabla de gastos
            encabezados_gastos = ['Código de Boleta', 'Tipo de Gasto', 'Área de Gasto', 'Fecha de Boleta', 'Monto Gastado']
            ancho_columnas_gastos = [100, 100, 100, 110, 110]

            # Posiciones iniciales para gastos
            y_actual_gastos = 750
            espaciado_entre_filas_gastos = 20

            # Dibujar encabezados para gastos
            for i, encabezado in enumerate(encabezados_gastos):
                p.drawString(ancho_columnas_gastos[i] * i + 10, y_actual_gastos, encabezado)

            # Dibujar datos para gastos
            for i, dato in enumerate(datos_gastos, start=1):
                y_actual_gastos -= espaciado_entre_filas_gastos
                for j, campo in enumerate(['Codigo_de_boleta', 'Tipo_de_gasto', 'Area_de_gasto', 'Fecha_boleta', 'Monto_gastado']):
                    valor = getattr(dato, campo)
                    if campo == 'Tipo_de_gasto':
                        valor = dato.get_Tipo_de_gasto_display()
                    elif campo == 'Area_de_gasto':
                        valor = dato.get_Area_de_gasto_display()
                    else:
                        valor = str(valor)
                    p.drawString(ancho_columnas_gastos[j] * j + 10, y_actual_gastos, valor)

                # Dibujar total para gastos al final de la tabla
                if i == len(datos_gastos):
                    y_actual_gastos -= espaciado_entre_filas_gastos
                    p.drawString(ancho_columnas_gastos[4] * 4 + 10, y_actual_gastos, f"Total Gastos: {total_gastos}")

            p.showPage()
            p.save()

            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)

            return response
        
        
        elif tipo_consulta == 'consultarIngresos':
            datos_ingresos = factura.objects.filter(Fecha_Emision__range=[fecha_inicio, fecha_fin])
            total_ingresos = datos_ingresos.aggregate(Sum('Importe'))['Importe__sum']

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="informe_contable_ingresos.pdf"'

            buffer = BytesIO()
            p = canvas.Canvas(buffer)

            # Estilos y formato para ingresos
            p.setFont("Helvetica", 9)

            # Título para INGRESOS centrado
            ancho_pagina, _ = p._pagesize
            ancho_titulo = p.stringWidth("INFORMES CONTABLES GENERALES", "Helvetica", 12)
            x_titulo = (ancho_pagina - ancho_titulo) / 2
            p.drawString(x_titulo, 800, "INFORMES CONTABLES GENERALES")
            
            # Título específico para INGRESOS centrado
            ancho_titulo_ingresos = p.stringWidth("INGRESOS", "Helvetica", 12)
            x_titulo_ingresos = (ancho_pagina - ancho_titulo_ingresos) / 2
            p.drawString(x_titulo_ingresos, 780, "INGRESOS")

            # Encabezados de la tabla de ingresos
            encabezados_ingresos = ['ID Cliente', 'Orden de Trabajo', 'Fecha de Emisión', 'IGV', 'Detracción', 'Importe']
            ancho_columnas_ingresos = [80, 90, 100, 100, 90, 90]

            # Posiciones iniciales para ingresos
            y_actual_ingresos = 750
            espaciado_entre_filas_ingresos = 20

            # Dibujar encabezados para ingresos
            for i, encabezado in enumerate(encabezados_ingresos):
                p.drawString(ancho_columnas_ingresos[i] * i + 10, y_actual_ingresos, encabezado)

            # Dibujar datos para ingresos
            for i, dato in enumerate(datos_ingresos, start=1):
                y_actual_ingresos -= espaciado_entre_filas_ingresos
                for j, campo in enumerate(['Id_cliente', 'Orden_de_trabajo', 'Fecha_Emision', 'IGV', 'Detraccion', 'Importe']):
                    p.drawString(ancho_columnas_ingresos[j] * j + 10, y_actual_ingresos, str(getattr(dato, campo)))

            # Dibujar total para ingresos
            y_actual_ingresos -= espaciado_entre_filas_ingresos
            p.drawString(ancho_columnas_ingresos[5] * 5 + 10, y_actual_ingresos, f"Total Ingresos: {total_ingresos}")

            p.showPage()
            p.save()

            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)

            return response

        elif tipo_consulta == 'consultarTotal':
            datos_gastos = gastos.objects.filter(Fecha_boleta__range=[fecha_inicio, fecha_fin])
            total_gastos = datos_gastos.aggregate(Sum('Monto_gastado'))['Monto_gastado__sum']

            datos_ingresos = factura.objects.filter(Fecha_Emision__range=[fecha_inicio, fecha_fin])
            total_ingresos = datos_ingresos.aggregate(Sum('Importe'))['Importe__sum']

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="informe_contable_total.pdf"'

            buffer = BytesIO()
            p = canvas.Canvas(buffer)

            # Estilos y formato para total
            p.setFont("Helvetica", 12)

            # Título para total centrado
            ancho_pagina, _ = p._pagesize
            ancho_titulo = p.stringWidth("INFORMES CONTABLES GENERALES", "Helvetica", 12)
            x_titulo = (ancho_pagina - ancho_titulo) / 2
            p.drawString(x_titulo, 800, "INFORMES CONTABLES GENERALES")



            # Título específico para gastos centrado
            ancho_titulo_gastos = p.stringWidth("Gastos", "Helvetica", 12)
            x_titulo_gastos = (ancho_pagina - ancho_titulo_gastos) / 2
            p.drawString(x_titulo_gastos, 780, "GASTOS")



            # Encabezados de la tabla de gastos
            encabezados_gastos = ['Código de Boleta', 'Tipo de Gasto', 'Área de Gasto', 'Fecha de Boleta', 'Monto Gastado']
            ancho_columnas_gastos = [100, 100, 100, 110, 110]

            # Posiciones iniciales para gastos
            y_actual_gastos = 750
            espaciado_entre_filas_gastos = 20

            # Dibujar encabezados para gastos
            for i, encabezado in enumerate(encabezados_gastos):
                p.drawString(ancho_columnas_gastos[i] * i + 10, y_actual_gastos, encabezado)

            # Dibujar datos para gastos
            for i, dato in enumerate(datos_gastos, start=1):
                y_actual_gastos -= espaciado_entre_filas_gastos
                for j, campo in enumerate(['Codigo_de_boleta', 'Tipo_de_gasto', 'Area_de_gasto', 'Fecha_boleta', 'Monto_gastado']):
                    valor = getattr(dato, campo)
                    if campo == 'Tipo_de_gasto':
                        valor = dato.get_Tipo_de_gasto_display()
                    elif campo == 'Area_de_gasto':
                        valor = dato.get_Area_de_gasto_display()
                    else:
                        valor = str(valor)
                    p.drawString(ancho_columnas_gastos[j] * j + 10, y_actual_gastos, valor)

                # Dibujar total para gastos al final de la tabla
                if i == len(datos_gastos):
                    y_actual_gastos -= espaciado_entre_filas_gastos
                    p.drawString(ancho_columnas_gastos[4] * 4 + 10, y_actual_gastos, f"Total Gastos: {total_gastos}")

            # Nueva página para la tabla de ingresos
            p.showPage()

            p.setFont("Helvetica", 9)
            # Título específico para ingresos centrado
            ancho_titulo_ingresos = p.stringWidth("Ingresos", "Helvetica", 12)
            x_titulo_ingresos = (ancho_pagina - ancho_titulo_ingresos) / 2
            p.drawString(x_titulo_ingresos, 800, "INGRESOS")

            # Encabezados de la tabla de ingresos
            encabezados_ingresos = ['ID Cliente', 'Orden de Trabajo', 'Fecha de Emisión', 'IGV', 'Detracción', 'Importe']
            ancho_columnas_ingresos = [80, 90, 100, 100, 90, 90]

            # Posiciones iniciales para ingresos
            y_actual_ingresos = 750
            espaciado_entre_filas_ingresos = 20

            # Dibujar encabezados para ingresos
            for i, encabezado in enumerate(encabezados_ingresos):
                p.drawString(ancho_columnas_ingresos[i] * i + 10, y_actual_ingresos, encabezado)

            # Dibujar datos para ingresos
            for i, dato in enumerate(datos_ingresos, start=1):
                y_actual_ingresos -= espaciado_entre_filas_ingresos
                for j, campo in enumerate(['Id_cliente', 'Orden_de_trabajo', 'Fecha_Emision', 'IGV', 'Detraccion', 'Importe']):
                    p.drawString(ancho_columnas_ingresos[j] * j + 10, y_actual_ingresos, str(getattr(dato, campo)))

                # Dibujar total para ingresos al final de la tabla
                if i == len(datos_ingresos):
                    y_actual_ingresos -= espaciado_entre_filas_ingresos
                    p.drawString(ancho_columnas_ingresos[5] * 5 + 10, y_actual_ingresos, f"Total Ingresos: {total_ingresos}")

            
            p.showPage()
            p.save()

            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)

            return response

    return render(request, 'ver_informes_contables.html')
