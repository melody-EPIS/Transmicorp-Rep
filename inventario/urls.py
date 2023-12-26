from django.urls import path 
from . import views 


urlpatterns = [ 
    path('crear/', views.crear_inventario, name='crear_inventario'), 
    path('ver_inventario/<int:pk>/', views.ver_inventario, name='ver_inventario'), 
    path('editar/<int:pk>/', views.editar_inventario, name='editar_inventario'), 
    path('eliminar/<int:pk>/', views.eliminar_inventario, name='eliminar_inventario'), 
    path('lista/', views.lista_inventario, name='lista_inventario'),
    path('generar_pdf/<int:pk>/', views.generar_pdf, name='generar_pdf'),
]