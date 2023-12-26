from django.urls import path 
from . import views 
urlpatterns = [ 
    path('crear/', views.crear_orden_trabajo, name='crear_orden_trabajo'), 
    path('ver/<int:pk>/', views.ver_orden_trabajo, name='ver_orden_trabajo'), 
    path('editar/<int:pk>/', views.editar_orden_trabajo, name='editar_orden_trabajo'), 
    path('eliminar/<int:pk>/', views.eliminar_orden_trabajo, name='eliminar_orden_trabajo'), 
    path('lista/', views.lista_ordenes_trabajo, name='lista_ordenes_trabajo'), 
]