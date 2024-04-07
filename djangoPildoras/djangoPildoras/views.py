from django.http import HttpResponse
import datetime

from django.template import Template, Context

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

    p1 = Persona("Profesor Juan", "Edaman")

    fecha_actual = datetime.datetime.now()


    doc_externo = open("/Users/ela/Desktop/DEVELOPER/DJANGO/LEARNING/djangoPildoras/djangoPildoras/plantillas/miplantilla.html")

    # doc_externo = open("djangoPildoras/djangoPildoras/plantillas/miplantilla.html")

    plantilla = Template(doc_externo.read())
    doc_externo.close()
    Contexto = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora_actual":fecha_actual,"temas":["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegues"]})
    documento = plantilla.render(Contexto)
    return HttpResponse(documento)
 



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