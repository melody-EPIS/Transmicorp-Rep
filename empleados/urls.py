from django.urls import path 
from . import views 
urlpatterns = [ 
    path('lista/', views.lista_empleados, name='lista_empleados'),
    path('crear/', views.crear_empleados, name='crear_empleados'), 
    path('ver/<int:pk>/', views.ver_empleados, name='ver_empleados'), 
    path('editar/<int:pk>/', views.editar_empleados, name='editar_empleados'), 
    path('eliminar/<int:pk>/', views.eliminar_empleados, name='eliminar_empleados'), 
]