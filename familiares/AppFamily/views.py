from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Familia
from django.template import Context, Template

# Create your views here.
def familiar(request, nombre, edad, fechaDeNac):
    familiar = Familia(nombre=nombre, edad=edad, fechaDeNac=fechaDeNac)
    familiar.save()

    return HttpResponse(f"""
        <p> Familiar: {familiar.nombre} -  {familiar.edad} - {familiar.fechaDeNac} --> agregado a la base! </p>
        """)

def lista_familia(request):
    lista = Familia.objects.all()

    return render(request, "lista_familia.html", {"lista_familia": lista})