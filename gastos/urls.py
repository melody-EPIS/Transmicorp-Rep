from django.urls import path 
from . import views

urlpatterns = [ 
    path('crear/', views.crear_gasto, name='crear_gasto'), 
    path('ver/<int:pk>/', views.ver_gasto, name='ver_gasto'), 
    path('editar/<int:pk>/', views.editar_gasto, name='editar_gasto'), 
    path('eliminar/<int:pk>/', views.eliminar_gasto, name='eliminar_gasto'), 
    path('lista/', views.lista_gasto, name='lista_gasto'), 
    path('ver_informes_contables/', views.ver_informes_contables, name='ver_informes_contables'), 
]