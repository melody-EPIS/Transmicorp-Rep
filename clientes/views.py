from django.shortcuts import render, redirect, get_object_or_404
from .models import clientes, clienteRUC10, clienteRUC20
from .forms import clientesForm, ClienteRUC10Form, ClienteRUC20Form
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def crear_clientes(request):
    if request.method == 'POST':
        form = clientesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = clientesForm()
    return render(request, 'crear_clientes.html', {'form': form})

#@login_required
#def ver_clientes(request, pk):
#    cliente = get_object_or_404(clientes, pk=pk)
#    return render(request, 'ver_clientes.html', {'cliente': cliente})

@login_required
def editar_clientes(request, pk):
    cliente_obj = get_object_or_404(clientes, pk=pk)
    if request.method == 'POST':
        form = clientesForm(request.POST, instance=cliente_obj)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes', pk=pk)
    else:
        form = clientesForm(instance=cliente_obj)
    return render(request, "editar_clientes.html", {'form': form, 'cliente': cliente_obj})

@login_required
def eliminar_clientes(request, pk):
    cliente_obj = get_object_or_404(clientes, pk=pk)
    if request.method == 'POST':
        cliente_obj.delete()
        return redirect('lista_clientes')
    return render(request, 'eliminar_clientes.html', {'cliente': cliente_obj})

@login_required
def lista_clientes(request):
    cliente = clientes.objects.all()
    return render(request, 'lista_clientes.html', {'cliente': cliente})
    
    
# Creacion de Formularios para TIPO RUC 10 y 20 
@login_required
def formulario_cliente_tipo(request):
    form_ruc10 = ClienteRUC10Form()
    form_ruc20 = ClienteRUC20Form()

    if request.method == 'POST':
        form_selected = request.POST.get("which_form_is_it")
        if form_selected == "ruc10":
            form_ruc10 = ClienteRUC10Form(request.POST)
            if form_ruc10.is_valid():
                form_ruc10.save()
                return redirect('lista_clientes')  # Redireccionar después de guardar exitosamente
        elif form_selected == "ruc20":
            form_ruc20 = ClienteRUC20Form(request.POST)
            if form_ruc20.is_valid():
                form_ruc20.save()
                return redirect('lista_clientes')  # Redireccionar después de guardar exitosamente

    return render(request, 'formulario_clientes.html', {'form_ruc10': form_ruc10, 'form_ruc20': form_ruc20})

# lista de datos declientes
@login_required 
def lista_clientes(request):
    cliente_ruc10_list = clienteRUC10.objects.all()
    cliente_ruc20_list = clienteRUC20.objects.all()
    return render(request, 'lista_clientes.html', {'cliente_ruc10_list': cliente_ruc10_list, 'cliente_ruc20_list': cliente_ruc20_list})

# Ver  cliente RUC10 

def detalle_cliente(request, pk):
    cliente_ruc10 = get_object_or_404(clienteRUC10, pk=pk)
    return render(request, 'ver_clientes.html', {'cliente_ruc10': cliente_ruc10})

# Ver  cliente  RUC20

def detalle_cliente_20(request, pk):
    cliente_ruc20 = get_object_or_404(clienteRUC20, pk=pk)
    return render(request, 'ver_clientes20.html', {'cliente_ruc20': cliente_ruc20})



# Editar  cliente RUC10
@login_required 
def editar_cliente_ruc_10(request, pk):
    cliente_ruc10 = get_object_or_404(clienteRUC10, pk=pk)
    
    if request.method == 'POST':
        form = ClienteRUC10Form(request.POST, instance=cliente_ruc10)
        if form.is_valid():
            form.save()
            return redirect('detalle_cliente', pk=pk)
    else:
        form = ClienteRUC10Form(instance=cliente_ruc10)
    
    return render(request, 'editar_clientes10.html', {'form': form, 'cliente_ruc10': cliente_ruc10})

# Editar  cliente RUC20
@login_required 
def editar_cliente_ruc_20(request, pk):
    cliente_ruc20 = get_object_or_404(clienteRUC20, pk=pk)
    
    if request.method == 'POST':
        form = ClienteRUC20Form(request.POST, instance=cliente_ruc20)
        if form.is_valid():
            form.save()
            return redirect('detalle_cliente_20', pk=pk)
    else:
        form = ClienteRUC20Form(instance=cliente_ruc20)
    
    return render(request, 'editar_cliente20.html', {'form': form, 'cliente_ruc20': cliente_ruc20})

