from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioLoginFormulario, RegistroFormulario
from django.shortcuts import render, redirect 

def inicio(request):

    return render(request, "portada.html")


def _1er_escenario(request):

    objetos = request.GET.get('objects', '0000')

    objetos_1 = list(objetos)

    context = {
    'objetos' : objetos_1,
    'objetosActuales': objetos,
    }
    return render(request, "Pieza.html", context)

def view(request):
  response = HttpResponse('blah')
  response.set_cookie('botellita', 'True')
  response.set_cookie('envoltorito', 'True')
  response.set_cookie('pizzita', 'True')
  response.set_cookie('papelito', 'True')

def _2do_escenario_1(request):

    objectsPrev = request.GET.get('objectsPrev', '0000')
    if "0" in objectsPrev:
        return redirect("/explosion2/")
    
    return render(request, "living.html")

def _2do_escenario_2(request):
    return render(request, "Casa.html")    

def _2do_escenario_3(request):
    return render(request, "Casa.html") 

def explosion(request):
    return render(request, "explosion.html")
def explosion2(request):
    return  render(request, "explosion2.html")
def parque(request):
    return render(request, "parque.html")
