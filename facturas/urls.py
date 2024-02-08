from django.urls import path
from . import views
urlpatterns = [
    path('verificar_facturas_pendientes/', views.verificar_facturas_pendientes, name='verificar_facturas_pendientes'),
    path('crear/', views.crear_factura, name='crear_factura'),
    path('ver/<int:pk>/', views.ver_factura, name='ver_factura'),
    path('editar/<int:pk>/', views.editar_factura, name='editar_factura'),
    path('eliminar/<int:pk>/', views.eliminar_factura, name='eliminar_factura'),
    path('lista/', views.lista_facturas, name='lista_facturas'),
    path('ver_pdf/<int:pk>/', views.ver_pdf, name='ver_pdf'),
]