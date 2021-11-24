from django.urls import path

from AppQuiz import views

urlpatterns = [
    path("",views.inicio, name="Portada"),
    path("pieza/",views._1er_escenario, name="1er"),
    path("casa1/",views._2do_escenario_1, name="2do_1"),
    path("casa2/",views._2do_escenario_2, name="2do_2"),
    path("casa3/",views._2do_escenario_3, name="2do_3"),
]
