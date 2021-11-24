from django.http.response import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "portada.html")

def _1er_escenario(request):
    return render(request, "Pieza.html")


def _2do_escenario_1(request):
    return render(request, "Casa.html")

def _2do_escenario_2(request):
    return render(request, "Casa.html")    

def _2do_escenario_3(request):
    return render(request, "Casa.html")    