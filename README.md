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


# Video 11 : BBDD

--> Django trabaja con varios tipos de  bases de datos 

1. SQLite 3 : Por defecto
2. PostgreSQL : Gestor recomendado 
3. MySQL
4. Oracle 

--> Con conectores ofrecidos por terceros 
1. SQL Server 
2. SAP SQL
3. DB2
4. Firebird
5. Etc


### Django distinque entre : Proyecto vs Apliacion 

a. Proyecto 
    ->(Tienda Online)
    -> Conjunto de aplicaciones

b. Apliacion 
    . Forma parte de un proyecto , osea esta dentro del proyectoo
    . Seria como 
        -> Un panel de contro de una web 
        -> Gestion de pagos
        -> Gestion de envios 
        -> Almacen Stock 
        -> Se encarga de las promocines 




### Proyecto - Ejemplo 

-> Tienda Online 

    --> App GestionPedidos 

        --> Tabla Cliente 
            . Nombre 
            . Direccion
            . Email
            .Tfno 

        --> Tabla Articulos 
            . Nombre 
            . Seccion 
            . Precio 

        --> Tabla Pedidos 
            . N_Pedido
            . Fechas 
            . Entregado


#### Como crear las tablas 

--> Apliacion (Dentro incluimos)

    --> Clase Model (Dentro incluimos las tablas )

        --> Tabla Clientes 
        --> Tabla Articulos 
        --> Tabla Pedidos


Es bueno crear apliaciones para administrar mejor un proyecto 


# Video 12 : BBDD II 

Es como se crea la apliacion y los primeros pasos a dar.

1. Despues de crear la aplicacion seguir 
2. "Models.py" crear las vistas 
3. "Settings.py"  registrar en "INSTALLED_APP" las apliacion que he creado
4. Para comprobar si todo va bien  desde la pagina de la aplicacion se puede poder donde esta el :  TiendaOnline gestionPedidos & Manage.py
    ==> python manage.py check gestionPedidos 
        . solucion: System check identified no issues (0 silenced).
        . Quiere deicir que todo esa bien


5. Creamos la base de datos con las tablas que hemos hecho antes de 
    . Clientes . Articulos . Pedidos

    ==> python manage.py makemigrations
        . solucion :
        Migrations for 'gestionPedidos':
            gestionPedidos/migrations/0001_initial.py
                - Create model Articulos
                - Create model Clientes
                - Create model Pedidos

    1 --> Con eso creamos la base de dato


    --> Luego de decimos a django que genere el codigo para hacer meterle las tablas 
        ==> python manage.py sqlmigrate gestionPedidos (numero de migracion  : ahora :0001)

        . Ahora tiene que aparecer en consola todas la instrucciones para crear tablas y que ya se a creado.

    2 --> Ahora hay que decirle que las tabla creadas que la meta en la base de datos
        ==>  python manage.py migrate

        .ahora si que ya tiene las tablas y todo dentro.


# Video 13 : BBDD III

Vamos a ver 

1.  Como insertar registros en la base de datos 
2. Actualizar registros 
3.  Borrar registros 


## 1  Insertar registros
--> Lo vamos hacer todo desde la consola.  Para acceder ponemos

    ==> python manage.py shell

    . Para meter la primera informacion en  la tabla mesa ponemor en shell

--> 1 Meter articulo 1 

    ==> from gestionPedidos.models import Articulos

    ==> art = Articulos (nombre = 'mesa', seccion = 'decoracion', precio = 90)

    ==>  art.save()

 --> 2 Meter articulo 2 

     ==> art2 = Articulos (nombre = 'camisa', seccion = 'confeccion' , precio = 75)

    ==> art2.save()

--> 3 Meter un nuevo articulo de una nueva forma
    ==> art3 = Articulos.objects.create (nombre='taladro', seccion = 'ferreteria', precio = 65)


    

## 2 Actulizar registro 
    ==>art.precio = 95

    ==>art.save()  


## 3 Borrar registro 
Dentro del parentesis especificar criterios, en este caso id = 2 
    ==>art5 = Articulos.objects.get(id=2)

    ==> art5.delete()
    .salida o silucion
        . (1, {'gestionPedidos.Articulos': 1})

## Consultas o ver una Query (select)

--> Crear una variable que sea y dentro hacer la consulta 
 en este caso : LISTA

    ==> lista = Articulos.objects.all()
    ==> lista

    . para verlo en el tipo select

    ==> lista.query.__str__()