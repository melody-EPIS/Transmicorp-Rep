from django.urls import path 
from . import views 
urlpatterns = [ 
    path('crear/', views.crear_proveedor, name='crear_proveedor'), 
    path('ver/<int:pk>/', views.ver_proveedor, name='ver_proveedor'), 
    path('editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'), 
    path('eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'), 
    path('lista/', views.lista_proveedores, name='lista_proveedores'), 
]