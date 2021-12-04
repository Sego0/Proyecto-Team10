from django.http.response import HttpResponse
from django.shortcuts import render, redirect

def inicio(request):
    return render(request, "portada.html")

def _1er_escenario(request):
    objetos = request.GET.get('objects', '0000000')
    if objetos == "1111":
        redirect("123")
    objetos_l = list(objetos)
    context = {
        "objetos" : objetos_l,
        "objetosAcualtes": objetos,
    }
    return render(request, "Pieza.html", context)

def _2do_escenario_1(request):
    return render(request, "Casa.html")

def _2do_escenario_2(request):
    return render(request, "Casa.html")    

def _2do_escenario_3(request):
    return render(request, "Casa.html")    