from django.http import HttpResponse
import datetime

from django.template import Template, Context


#Esta es una funcion vista o la primera vista
def saludo(request):

    #nombre 
    nombre = "Juan"
    apellido = "Ndumu Osa"

    doc_externo = open("/Users/ela/Desktop/DEVELOPER/DJANGO/LEARNING/djangoPildoras/djangoPildoras/plantillas/miplantilla.html")

    # doc_externo = open("djangoPildoras/djangoPildoras/plantillas/miplantilla.html")

    plantilla = Template(doc_externo.read())
    doc_externo.close()
    Contexto = Context({"nombre_persona":nombre, "apellido_persona":apellido})
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