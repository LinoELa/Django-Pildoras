"""
URL configuration for djangoPildoras project.

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
from django.contrib import admin
from django.urls import path

#from <carpeta.archivo> import <funcion>,<funcion2>
from djangoPildoras.views import saludo,despedida, dameFecha, calculaEdad, calculaEdad_2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    #el nombre de la url puede ser diferente al de la funcion
    path('nosvemos/', despedida),  #despedida es diferente a lo  URL= nosVemos

    path('fecha/', dameFecha),
    # una forma de pasar la url a entero > es poniendole ( : ) delante
    path('edades/<int:axo>', calculaEdad),

    # Otra forma de de recibir paramtro por URL
    path('edades/<int:edad>/<int:axo>', calculaEdad_2)
    
]
