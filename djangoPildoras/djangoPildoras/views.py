from django.http import HttpResponse
import datetime

from django.template import Template, Context
from django.template.loader import get_template #sirve para cargar plantillas

from django.shortcuts import render




# usando la programacion orientada  a objetos 

class Persona(object):
    def __init__(self, nombre , apellido):
        self.nombre = nombre 
        self.apellido = apellido
        
 


#Esta es una funcion vista o la primera vista
def saludo(request):


    #nombre  --> Comentamos todo eso para mostras lo siguiente 
    # nombre = "Juan"
    # apellido = "Ndumu Osa"

    # --> Comentamos todo eso para mostras lo siguiente

    temas_del_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegues"] #con informacion  : datos
    # temas_del_curso = []  #vacio

    p1 = Persona("Profesor Juan", "Edaman")

    fecha_actual = datetime.datetime.now()

    # doc_externo = open("/Users/ela/Desktop/DEVELOPER/DJANGO/LEARNING/djangoPildoras/djangoPildoras/plantillas/miplantilla.html")
    # plantilla = Template(doc_externo.read())
    # doc_externo.close()
    # Contexto = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora_actual":fecha_actual,"temas":temas_del_curso})
    # documento = plantilla.render(Contexto)
    # return HttpResponse(documento)

    """ pra no usar doc_externo = open("/Users/ela/Desktop/DEVELOPER/DJANGO/LEARNING/djangoPildoras/djangoPildoras/plantillas/miplantilla.html 
    Podemmos usar un cargador de plantillas

    # Se hace de la siguiente forma 
    
    """ 

# CARGAR LA PLANTILLAA EXTERNA : de forma 
    # doc_externo_cargar_plantilla = get_template('miplantilla.html')
    # rederizar_documento = doc_externo_cargar_plantilla.render({ "nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora_actual":fecha_actual,"temas":temas_del_curso})
    # return HttpResponse(rederizar_documento)

# CARGAR LA PLANTILLAA EXTERNA II : de forma mas sencilla

    return render (request, 'miplantilla.html',{ "nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora_actual":fecha_actual,"temas":temas_del_curso})



 

#Crear una nueva vista para las las las nuevas plantillas que heredan

def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'CursoC.html', {"dameFecha":fecha_actual})

def cursoCss(request):
    fecha_actual = datetime.datetime.now()
    return render (request, "cursoCss.html", {"fecha_actual":fecha_actual})

def despedida(request):
    return HttpResponse("Despedida")


def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    variable_datetime = """
    <body>
    <h1>Fecha actuales %s </h1>
    </body>
    </html> """ % fecha_actual

    return HttpResponse(variable_datetime)

#vamos a recibir un parametro anadicional
def calculaEdad(request, axo):
    edadActual = 18
    periodo = axo - 2019
    edadFutura = edadActual + periodo

    edades = """
    <h1>En el axo %s tendras %s axos </h1>
    </body>
    </html> 
    """ % (axo, edadFutura)

    return HttpResponse(edades)

# Otra forma de recivir parametros desde la url
def calculaEdad_2 (request,edad, axo):
    # edadActual = 18
    periodo = axo - 2019
    edadFutura = edad + periodo

    edades = """
    <h1>En el axo %s tendras %s axos </h1>
    </body>
    </html> 
    """ % (axo, edadFutura)

    return HttpResponse(edades)