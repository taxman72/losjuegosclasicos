from django.shortcuts import render
import datetime
from django.http import HttpResponse


def home(request):
    return render(request, 'miweb/index.html')


def saludo(request):
    """return HttpResponse("Hello, world. You're at the polls index.")"""
    return HttpResponse("Hello, world. You're at the polls index.")

def dame_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calcula_edad(request,agno):
    periodo=agno-2021
    edadactual=18
    edadfutura=edadactual+periodo
    documento="""<html>
    <body>
    <h1>
    En el año %s tendras %s años tontito
    </h1>
    </body>
    </html>""" %(agno,edadfutura)
    return HttpResponse(documento)

def boton(request):
    documento="""<html>
    <body>
    <label class="switch">
  <input type="checkbox">
  <span class="slider"></span>
    </label>
    </body>
    </html>"""
    return HttpResponse(documento)
