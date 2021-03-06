"""ClaseDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', saludo),
    path('otra-vista/', otra_vista), #Al no poner argumento entre "" va directo a la pagina raiz
    path('fecha-actual/', fecha_actual),
    #path('<str:nombre>/', saludo_a), Jerarquias de urls
    path('saludo-a/<nombre>', saludo_a),
    path('<int:edad>/<str:nombre>', anio_nacimiento),
    path('probandoTemplate/', probandoTemplate),

    path('admin/', admin.site.urls),
]
