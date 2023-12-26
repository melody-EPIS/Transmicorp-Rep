from django.urls import path 
from . import views

urlpatterns = [ 
    path('lista/', views.lista_unidades, name='lista_unidades'),
    path('crear/', views.crear_unidad, name='crear_unidad'), 
    path('ver/<int:pk>/', views.ver_unidad, name='ver_unidad'), 
    path('editar/<int:pk>/', views.editar_unidad, name='editar_unidad'), 
    path('eliminar/<int:pk>/', views.eliminar_unidad, name='eliminar_unidad'), 
     
]