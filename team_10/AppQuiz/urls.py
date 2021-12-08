from django.urls import path

from .views import explosion2,parque,inicio,_1er_escenario,_2do_escenario_1,_2do_escenario_2,_2do_escenario_3,explosion

urlpatterns = [
    path("", inicio, name="portada"),

    
    path("pieza/",_1er_escenario, name="1er"),
    path("casa1/",_2do_escenario_1, name="2do_1"),
    path("casa2/",_2do_escenario_2, name="2do_2"),
    path("casa3/",_2do_escenario_3, name="2do_3"),
    path("parque", parque, name="parque"),
    path("explosion/",explosion, name="explosion"),
    path("explosion2/", explosion2, name="explosion2")
]
