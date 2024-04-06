from django.http import HttpResponse
import datetime

#Esta es una funcion vista o la primera vista
def saludo(request):
    #una forma as elegane es crear una variable y meter el html dentro

    # documento = "<body><h1>Hola alumnos de pildoras Informaticas</h1></body></html>"

    # return HttpResponse(documento)

    documento = """
    <body>
    <h1>Hola alumnos de pildoras Informaticas forma 2</h1>
    </body>
    </html> """

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