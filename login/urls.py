from django.urls import path 
from .views import crear_cuenta

urlpatterns = [ 
    path('crear_cuenta', crear_cuenta, name='crear_cuenta'), 
     
]