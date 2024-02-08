from django.shortcuts import render, redirect, get_object_or_404
from .models import gastos
from .forms import GastosForm
from facturas.models import factura
from facturas.forms import FacturaForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.db.models import Sum

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
import os
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
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []
            def encabezado2(canvas, doc):
                script_dir = os.path.dirname(__file__)
                logo_path = os.path.join(script_dir, 'logo.png')
                logo = ImageReader(logo_path)
                canvas.saveState()

                # Dimensiones del logo
                logo_width, logo_height = 1.5 * inch, 1.5 * inch  # Ajusta según sea necesario

                # Dibuja el logo en la esquina superior izquierda
                canvas.drawImage(logo, 0, doc.pagesize[1] - logo_height, width=logo_width, height=logo_height, preserveAspectRatio=True)

                # Configuración de la fuente para el texto
                canvas.setFont('Helvetica-Bold', 20)

                # Texto a dibujar
                text = "Transmicorp S.A.C"

                # Coordenadas para el texto
                text_x = logo_width + 100  # Ajusta según sea necesario
                text_y = doc.pagesize[1] - 0.5 * inch  # Ajusta según sea necesario

                # Dibuja el texto
                canvas.drawString(text_x, text_y, text)
                
                # Agregar pie de página
                direccion1 = "Mza. Ñ Loote 8 URB Alas del Sur"
                direccion2 = "Arequipa-Arequipa Jose Luis Bustamente y Rivero"
                contacto1 = "Contacto: +123456789"
                contacto2 = "correo@ejemplo.com"

                # Coordenadas para la dirección y el contacto
                direccion_x = 20  # Ajusta según sea necesario
                contacto_x = doc.pagesize[0] - 200  # Ajusta según sea necesario
                pie_y = 20  # Ajusta según sea necesario

                # Dibuja la dirección y el contacto
                canvas.setFont('Helvetica', 10)
                canvas.drawString(direccion_x, pie_y, direccion1)
                # Ajusta la coordenada Y para la segunda línea de dirección
                pie_y -= 12  # Ajusta según sea necesario para el espaciado entre líneas
                canvas.drawString(direccion_x, pie_y, direccion2)

                # Coordenadas para los contactos
                contacto1_x = doc.pagesize[0] - 200  # Ajusta según sea necesario
                contacto2_x = doc.pagesize[0] - 200  # Ajusta según sea necesario
                # Ajusta la coordenada Y para contacto1
                pie_y = 20  # Ajusta según sea necesario para el espaciado entre líneas
                canvas.drawString(contacto1_x, pie_y, contacto1)
                # Ajusta la coordenada Y para contacto2
                pie_y -= 12  # Ajusta según sea necesario para el espaciado entre líneas
                canvas.drawString(contacto2_x, pie_y, contacto2)

                canvas.restoreState()
                
                
            # Estilos y formato para gastos
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'Title',
                parent=styles['Title'],
                fontName='Helvetica-Bold',  # Puedes cambiar la fuente según tus preferencias
                fontSize=14,
                spaceAfter=12,
            )

            # Título para GASTOS centrado

            elements.append(Paragraph("INFORMES CONTABLES GENERALES", title_style))
            elements.append(Paragraph("GASTOS", title_style))


            # Encabezados de la tabla de gastos
            encabezados_gastos = ['Código de Boleta', 'Tipo de Gasto', 'Área de Gasto', 'Fecha de Boleta', 'Monto Gastado']

            # Datos para la tabla de gastos
            # Datos para la tabla de gastos
            datos_tabla_gastos = [
                [encabezado.upper() for encabezado in encabezados_gastos],
                *[
                    [
                        getattr(dato, campo) if campo != 'Tipo_de_gasto' and campo != 'Area_de_gasto' else dato.get_Tipo_de_gasto_display() if campo == 'Tipo_de_gasto' else dato.get_Area_de_gasto_display() 
                        for campo in ['Codigo_de_boleta', 'Tipo_de_gasto', 'Area_de_gasto', 'Fecha_boleta', 'Monto_gastado']
                    ]
                    for dato in datos_gastos
                ],
                ['', '', '', 'Total Gastos:', total_gastos],  # Fila para el total
            ]

            # Crear la tabla
            tabla_gastos = Table(datos_tabla_gastos)
            tabla_gastos.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -2), colors.white),
                ('GRID', (0, 0), (-1, -2), 1, colors.black)
            ]))

            elements.append(tabla_gastos)

            # Dibujar total para gastos al final de la tabla
            #elements.append(Paragraph(f"Total Gastos: {total_gastos}", styles['Normal']))

            doc.build(elements,
                      onFirstPage=encabezado2,
                      onLaterPages=encabezado2)

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
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []
            def encabezado2(canvas, doc):
                script_dir = os.path.dirname(__file__)
                logo_path = os.path.join(script_dir, 'logo.png')
                logo = ImageReader(logo_path)
                canvas.saveState()

                # Dimensiones del logo
                logo_width, logo_height = 1.5 * inch, 1.5 * inch  # Ajusta según sea necesario

                # Dibuja el logo en la esquina superior izquierda
                canvas.drawImage(logo, 0, doc.pagesize[1] - logo_height, width=logo_width, height=logo_height, preserveAspectRatio=True)

                # Configuración de la fuente para el texto
                canvas.setFont('Helvetica-Bold', 20)

                # Texto a dibujar
                text = "Transmicorp S.A.C"

                # Coordenadas para el texto
                text_x = logo_width + 100  # Ajusta según sea necesario
                text_y = doc.pagesize[1] - 0.5 * inch  # Ajusta según sea necesario

                # Dibuja el texto
                canvas.drawString(text_x, text_y, text)
                
                # Agregar pie de página
                direccion1 = "Mza. Ñ Loote 8 URB Alas del Sur"
                direccion2 = "Arequipa-Arequipa Jose Luis Bustamente y Rivero"
                contacto1 = "Contacto: +123456789"
                contacto2 = "correo@ejemplo.com"

                # Coordenadas para la dirección y el contacto
                direccion_x = 20  # Ajusta según sea necesario
                contacto_x = doc.pagesize[0] - 200  # Ajusta según sea necesario
                pie_y = 20  # Ajusta según sea necesario

                # Dibuja la dirección y el contacto
                canvas.setFont('Helvetica', 10)
                canvas.drawString(direccion_x, pie_y, direccion1)
                # Ajusta la coordenada Y para la segunda línea de dirección
                pie_y -= 12  # Ajusta según sea necesario para el espaciado entre líneas
                canvas.drawString(direccion_x, pie_y, direccion2)

                # Coordenadas para los contactos
                contacto1_x = doc.pagesize[0] - 200  # Ajusta según sea necesario
                contacto2_x = doc.pagesize[0] - 200  # Ajusta según sea necesario
                # Ajusta la coordenada Y para contacto1
                pie_y = 20  # Ajusta según sea necesario para el espaciado entre líneas
                canvas.drawString(contacto1_x, pie_y, contacto1)
                # Ajusta la coordenada Y para contacto2
                pie_y -= 12  # Ajusta según sea necesario para el espaciado entre líneas
                canvas.drawString(contacto2_x, pie_y, contacto2)

                canvas.restoreState()


            # Estilos y formato para ingresos
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'Title',
                parent=styles['Title'],
                fontName='Helvetica-Bold',
                fontSize=14,
                spaceAfter=12,
            )

            # Título para INGRESOS centrado
            elements.append(Paragraph("INFORMES CONTABLES GENERALES", title_style))
            elements.append(Paragraph("INGRESOS", title_style))

            # Encabezados de la tabla de ingresos
            encabezados_ingresos = ['ID Cliente', 'Orden de Trabajo', 'Fecha de Emisión', 'IGV', 'Detracción', 'Importe']

            # Datos para la tabla de ingresos
            datos_tabla_ingresos = [
                [encabezado.upper() for encabezado in encabezados_ingresos],
                *[
                    [str(getattr(dato, campo)) for campo in ['Id_cliente', 'Orden_de_trabajo', 'Fecha_Emision', 'IGV', 'Detraccion', 'Importe']]
                    for dato in datos_ingresos
                ],
                ['', '', '', '', '', f'Total Ingresos: {total_ingresos}'],  # Fila para el total
            ]

            # Crear la tabla
            tabla_ingresos = Table(datos_tabla_ingresos)
            tabla_ingresos.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -2), colors.white),
                ('GRID', (0, 0), (-1, -2), 1, colors.black),
            ]))

            elements.append(tabla_ingresos)

            doc.build(elements,
                      onFirstPage=encabezado2,
                      onLaterPages=encabezado2)

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
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []
            def encabezado2(canvas, doc):
                script_dir = os.path.dirname(__file__)
                logo_path = os.path.join(script_dir, 'logo.png')
                logo = ImageReader(logo_path)
                canvas.saveState()

                # Dimensiones del logo
                logo_width, logo_height = 1.5 * inch, 1.5 * inch  # Ajusta según sea necesario

                # Dibuja el logo en la esquina superior izquierda
                canvas.drawImage(logo, 0, doc.pagesize[1] - logo_height, width=logo_width, height=logo_height, preserveAspectRatio=True)

                # Configuración de la fuente para el texto
                canvas.setFont('Helvetica-Bold', 20)

                # Texto a dibujar
                text = "Transmicorp S.A.C"

                # Coordenadas para el texto
                text_x = logo_width + 100  # Ajusta según sea necesario
                text_y = doc.pagesize[1] - 0.5 * inch  # Ajusta según sea necesario

                # Dibuja el texto
                canvas.drawString(text_x, text_y, text)
                
                # Agregar pie de página
                direccion1 = "Mza. Ñ Loote 8 URB Alas del Sur"
                direccion2 = "Arequipa-Arequipa Jose Luis Bustamente y Rivero"
                contacto1 = "Contacto: +123456789"
                contacto2 = "correo@ejemplo.com"

                # Coordenadas para la dirección y el contacto
                direccion_x = 20  # Ajusta según sea necesario
                contacto_x = doc.pagesize[0] - 200  # Ajusta según sea necesario
                pie_y = 20  # Ajusta según sea necesario

                # Dibuja la dirección y el contacto
                canvas.setFont('Helvetica', 10)
                canvas.drawString(direccion_x, pie_y, direccion1)
                # Ajusta la coordenada Y para la segunda línea de dirección
                pie_y -= 12  # Ajusta según sea necesario para el espaciado entre líneas
                canvas.drawString(direccion_x, pie_y, direccion2)

                # Coordenadas para los contactos
                contacto1_x = doc.pagesize[0] - 200  # Ajusta según sea necesario
                contacto2_x = doc.pagesize[0] - 200  # Ajusta según sea necesario
                # Ajusta la coordenada Y para contacto1
                pie_y = 20  # Ajusta según sea necesario para el espaciado entre líneas
                canvas.drawString(contacto1_x, pie_y, contacto1)
                # Ajusta la coordenada Y para contacto2
                pie_y -= 12  # Ajusta según sea necesario para el espaciado entre líneas
                canvas.drawString(contacto2_x, pie_y, contacto2)

                canvas.restoreState()
            # Estilos y formato para total
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'Title',
                parent=styles['Title'],
                fontName='Helvetica-Bold',
                fontSize=14,
                spaceAfter=12,
            )

            # Título para GASTOS centrado
            elements.append(Paragraph("INFORMES CONTABLES GENERALES", title_style))

            # Título específico para gastos centrado
            elements.append(Paragraph("GASTOS", title_style))

            # Encabezados de la tabla de gastos
            encabezados_gastos = ['Código de Boleta', 'Tipo de Gasto', 'Área de Gasto', 'Fecha de Boleta', 'Monto Gastado']

            # Datos para la tabla de gastos
            # Datos para la tabla de gastos
            datos_tabla_gastos = [
                [encabezado.upper() for encabezado in encabezados_gastos],
                *[
                    [
                        getattr(dato, campo) if campo != 'Tipo_de_gasto' and campo != 'Area_de_gasto' else dato.get_Tipo_de_gasto_display() if campo == 'Tipo_de_gasto' else dato.get_Area_de_gasto_display() 
                        for campo in ['Codigo_de_boleta', 'Tipo_de_gasto', 'Area_de_gasto', 'Fecha_boleta', 'Monto_gastado']
                    ]
                    for dato in datos_gastos
                ],
                ['', '', '', 'Total Gastos:', total_gastos],  # Fila para el total
            ]

            # Crear la tabla
            tabla_gastos = Table(datos_tabla_gastos)
            tabla_gastos.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -2), colors.white),
                ('GRID', (0, 0), (-1, -2), 1, colors.black),
            ]))

            elements.append(tabla_gastos)

            # Nueva página para la tabla de ingresos
            elements.append(Paragraph("INGRESOS", title_style))

            # Encabezados de la tabla de ingresos
            encabezados_ingresos = ['ID Cliente', 'Orden de Trabajo', 'Fecha de Emisión', 'IGV', 'Detracción', 'Importe']

            # Datos para la tabla de ingresos
            datos_tabla_ingresos = [
                [encabezado.upper() for encabezado in encabezados_ingresos],
                *[
                    [str(getattr(dato, campo)) for campo in ['Id_cliente', 'Orden_de_trabajo', 'Fecha_Emision', 'IGV', 'Detraccion', 'Importe']]
                    for dato in datos_ingresos
                ],
                ['', '', '', '', '', f'Total Ingresos: {total_ingresos}'],  # Fila para el total
            ]

            # Crear la tabla
            tabla_ingresos = Table(datos_tabla_ingresos)
            tabla_ingresos.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -2), colors.white),
                ('GRID', (0, 0), (-1, -2), 1, colors.black),
            ]))

            elements.append(tabla_ingresos)

            doc.build(elements,
                      onFirstPage=encabezado2,
                      onLaterPages=encabezado2)

            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)

            return response

    return render(request, 'ver_informes_contables.html')


