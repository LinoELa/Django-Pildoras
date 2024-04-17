# Django-Pildoras

# Video 5 : Plantilla I

Como unir HTML con Django


# Video 6: Plantilla II

El video 6 es muy importante porque habla de variables y propiedades en django, asi  como clases y como poder trabajar la parte logica del video por detras y la parte visible el HTML por delante.


Uso de variblaes en plantillas
Acceeso aa objetos y propiedades desde plantillas
    uso de diccionarios en contexto

Tambien se ha hablado de como enviar informacion variables de una varible de un archivo.py a un archivo.html 

En la parte 3 se crea instancias.


###Clases 
se habla de las clases en el video 6 y es muy importante para ser sobre contructor __init__ y mas mas  cosas de uso de una clase


# Video 7 : Plantillas III
El video 7 se enfoca en los buvles y condicionales en planntillas  y sus puntos principales son

###Llamadas a plantillas 
    Jerarquia u orden en llamadas desde plantillas
        .Diccionario
        .Atributo
        .Metodo
        .indice de lista

###uso de listas en contexto y plantillas 

###Estructura de contro de flujo (Bucles y condicionales)


si que es posible anidar todo en bucles : for , if , while y mas.

##Ejemplos de cada tipo de elemento

###Diccionario 
-->Diccionario que mapea nombres de frutas a sus colores

frutas_colores = {
    "manzana": "rojo",
    "plátano": "amarillo",
    "naranja": "naranja"
}

-->Accediendo al valor asociado a una clave
print(frutas_colores["manzana"])  # Salida: rojo

###Atributo 
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo nombre
        self.raza = raza  # Atributo raza

-->Creando una instancia de la clase Perro
mi_perro = Perro("Max", "Labrador")

-->Accediendo a los atributos de la instancia
print(mi_perro.nombre)  # Salida: Max
print(mi_perro.raza)    # Salida: Labrador

###Metodo

--> .upper() : 
--> .lower() :
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2

-->Creando una instancia de la clase Circulo
mi_circulo = Circulo(5)

-->Llamando al método calcular_area()
print(mi_circulo.calcular_area())  # Salida: 78.5

###Indice de lista
-->Definiendo una lista de colores
colores = ["rojo", "verde", "azul", "amarillo"]

-->Accediendo al elemento en el índice 2 (que es "azul")
print(colores[2])  # Salida: azul

###Filtros 
https://docs.djangoproject.com/en/5.0/ref/templates/builtins/

                <li>{{elTema  | first | lower }}</li>

# Video 8 : Plantillas IV => Cargar plantillas

###cargar plantillas en vez de 
doc_externo = open("/Users/ela/Desktop/DEVELOPER/DJANGO/LEARNING/djangoPildoras/djangoPildoras/plantillas/miplantilla.html"
usar un cargador de plantillas

.--> Es la url de como cargar varias plantillas sin necesidad de usar url tan largar : https://youtu.be/BcoPWMtmgJk?si=2gLuxvRRm9cgbzNP&t=867


# Video 9 : Plantillas V => Shortcuts & Plantillas uno dentro de otro 
### Es la mejor forma de cargar plantillas 

que veremos  ver 
. simplificacion del codigo con paquetes shortcuts 
. Plantillas incrustadas (plantillas dentro de plantillas)

--> Pagina de shortcuts de django
https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/

Es para saber como simplificar el codigo

--> Cargar plantilla seria  <-- 
from django.shortcuts import render

    return render (request, 'miplantilla.html',{ "nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora_actual":fecha_actual,"temas":temas_del_curso})

--> Fin <-- 

### Barra.html -> Plantillas incrustadas
https://youtu.be/Opm8KKR99kQ?si=Pnzx0whkT6qlWNfI&t=277

Cuando creamos una pagina y queremos que una barra aparezca en 20 paginas pues creamos esta barra en un html y lo incrustamos dentro de la plantilla.

-> Creamos una nueva plantilla de nombre barra.html


1. Creamos la pagina : barra.html
2. Determinados donde queremos que aparezca 
3. la incrustamos con {% include "barra.html" %} 
    a. En caso que este dentro de una carpeta : {% include "superior/barra.html" %} 
4. 







# Video 10 : Herencia de plantillas 

para decirle a una plantilla que tiene que heredar de una padre seria ponerle 

-> {% extends "nombre_plantilla.html"%}

Osa es como crear una pagina padre donde le podemos poner el nav y el footer y cada pagina que creemos desde ella  siempre llevara lo que hemos creado.

-> Necesita mucha practica esta parte para entenderlo mejor