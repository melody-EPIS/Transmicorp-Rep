from django.urls import path 
from . import views

urlpatterns = [ 
    path('lista/', views.lista_clientes, name='lista_clientes'),
    path('crear/', views.crear_clientes, name='crear_clientes'), 
    path('ver1/<int:pk>/', views.detalle_cliente, name='detalle_cliente'), 
    path('ver2/<int:pk>/', views.detalle_cliente_20, name='detalle_cliente_20'), 
    path('editar/<int:pk>/', views.editar_clientes, name='editar_clientes'), 
    path('editar10/<int:pk>/', views.editar_cliente_ruc_10, name='editar_cliente_ruc_10'), 
    path('editar20/<int:pk>/', views.editar_cliente_ruc_20, name='editar_cliente_ruc_20'), 
    path('eliminar/<int:pk>/', views.eliminar_clientes, name='eliminar_clientes'), 
    path('crear_tipo/', views.formulario_cliente_tipo, name='formulario_cliente_tipo'),
     
]
