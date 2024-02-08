"""
URL configuration for ProyectoTransmicorp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from login.views import base, salir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),#login
    path('salir/', salir, name = "salir"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('orden_de_trabajo/', include('orden_de_trabajo.urls')),
    path('facturas/', include('facturas.urls')),
    path('inventario/', include('inventario.urls')),
    path('clientes/', include('clientes.urls')),
    path('unidades/', include('unidades.urls')),
    path('gastos/', include('gastos.urls')),
    path('notificaciones/', include('notificaciones.urls')),
    path('empleados/', include('empleados.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('account/', include('account.urls')),
    path('login/', include('login.urls')),
    path('_debug_/', include(debug_toolbar.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
