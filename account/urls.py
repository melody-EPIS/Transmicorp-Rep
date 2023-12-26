from django.urls import path 
from .views import user_profile, settings, editar_perfil

urlpatterns = [ 
    path('', user_profile, name='user_profile'),
    path('settings', settings, name='settings'),
    path('editar/', editar_perfil, name='editar_perfil'),
     
]