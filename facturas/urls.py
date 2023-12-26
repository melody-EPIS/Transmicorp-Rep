from django.urls import path 
from . import views 
urlpatterns = [ 
    path('crear/', views.crear_factura, name='crear_factura'), 
    path('ver/<int:pk>/', views.ver_factura, name='ver_factura'), 
    path('editar/<int:pk>/', views.editar_factura, name='editar_factura'), 
    path('eliminar/<int:pk>/', views.eliminar_factura, name='eliminar_factura'), 
    path('lista/', views.lista_facturas, name='lista_facturas'), 
]