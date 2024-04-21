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



# Video 14 :  PostgreSQL en local

### Como usar PostgreSQL
https://www.youtube.com/watch?v=UjQiwonRMas


https://youtu.be/jMPTz5NWIPY?list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB

1.  Como configurar Django con PostgreSQL en local

Es open source

Primero vamos a necesitar una interfaz 

--> El modo de uso esta en este video : 
https://youtu.be/jMPTz5NWIPY?list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB

--> Intrucir registros y datos 
    Para hacerlo
    1.  Tenemos que conectar la base de datos con nuestro proyecto
    2. Para hacerlo tenemos que instalar la una libreria : --> PSYCOPG2 <--
    3. Para instalarla vamos a al directorio del proyecto en este caso : 
        . TiendaOnline 
        introducimos  :
        ==> pip install psycopg2

        A. --> Si hay un error pues usar <--

        ==> brew install postgresql
        ==> pg_config --version
        ==> pip install psycopg2

2. Cambiar la  configuracion en settings.py para que nuestra proyecto en django se conecte con esta base de datos 

--> Como se hace ?

Pues en settings.py cambiar el ENGINE , NAME  y AGREGAR unos parametros  mas dentro del DATABSES de settings.py

--> settigs.py antiguo <-- 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} 

--> settigs.py NUEVO <-- 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ArticulosClientes',
        'USER': 'postgres',
        'PASSWORD': '123456789',
        'HOST': '127.0.0.1',
        'DATABASE': '5432',
    }
}

--> AHORA LO MISMO QUE SQLite3 <-- 
1. Creamos las tablas 

# Video 15 - 20 : Panel del Administracion

Hablan del todo  lo que se puede hacer en el panel de administracion , asi como las se puedee añadir o n usuarios, 
filtros , y mas cosas. 

# Video 21 : Formularios I
https://youtu.be/B840ou6pcjg?si=zewOem43KnVF4QMn


--> Trabajos con formularios 
    -> Creacion de formularios (Manual) y envio de datos al servidor
        -> Objetos HttpResponse


        Request : es para enviar una informacion al servidor 
        el servidor puede manipular el elemento request

        Pigina principal 
        https://docs.djangoproject.com/en/5.0/ref/request-response/


        Los dos metodos principales son 
        1.  Get 
        2.  Post

        Como enviar documentos a otra pagina 

        AL final de todo hemos aprendido como introducir informacion a un formulario y que este formulario viaje a travez del servidor. 


# Video 22: Formulario II

--> Ya que en el video 21 vimos como introducir informacion a un formulario y que este formulario viaje a travz del servidor , pues esta clase va de : 

1. Como Buscar informacion en una base de datos.
    la informacion viene del formulario.

    Conseguimos acceder a la base de datos y recoger infacion almacenada en ella y poder motrarlo en la en la vista 

# Video 23 : Formulario III

1.  Limitar el numero de caracteres o letras o longitud en formularios a buscar en BBDD 

2.  Crear un formulario de contacto (1å Parte)


Limitar la longitud seria : 

=> if len(producto ) > 20: 
    mensaje = 'Texto demasiado largo'
else : 
    lo que de verdad queiro que se veas 

--- 


--> Vamos a configurar el servidor de pruebas para que sea capaz de enviarlos un correo electronico 

# Video 24 : EMAIL

--> Envio de Email con Django 

usaremos un una librerias 

    -> CORE.MAIL


1. Tenemos que buscar un servidor para enviar correos 
2. Configurar el correo electronico para que pueda enviar mensaje  desde sercicios de terceros
3. Configuar Email en Django 


# Video 25 : API Forms
https://docs.djangoproject.com/en/5.0/ref/forms/api/

Lo que nos ayuda es en simplificar mucho la creacion de un formulario 
y la Email sera validada

La API Forms ayuda a validar el correo para que no nos llegue spam


--> Se tiene que crear un archivo llamado FORMS
y dentro importamos forms 

==> from django import forms 

--> Es mejor utiliarlo <--


