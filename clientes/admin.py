from ast import Or
from django.contrib import admin
from .models import clientes, clienteRUC10, clienteRUC20
# Register your models here.

admin.site.register(clientes)
admin.site.register(clienteRUC10)
admin.site.register(clienteRUC20)
