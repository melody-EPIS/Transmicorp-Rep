from django.urls import path 
from . import views 
urlpatterns = [ 
    path('crear/', views.crear_notificaciones, name='crear_notificaciones'), 
    path('ver/<int:pk>/', views.ver_notificaciones, name='ver_notificaciones'), 
    path('editar/<int:pk>/', views.editar_notificaciones, name='editar_notificaciones'), 
    path('eliminar/<int:pk>/', views.eliminar_notificaciones, name='eliminar_notificaciones'), 
    path('lista/', views.lista_notificaciones, name='lista_notificaciones'), 
]