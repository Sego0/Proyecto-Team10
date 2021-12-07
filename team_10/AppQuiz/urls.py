from django.urls import path

from .views import inicio,loginView,logout_vista,registro,_1er_escenario,_2do_escenario_1,_2do_escenario_2,_2do_escenario_3,explosion

urlpatterns = [
    path("", inicio, name="portada"),

    path('login/', loginView, name='login'),
    path('logout_vista/', logout_vista, name='logout_vista'),
    path('registro/', registro, name='registro'),

    path("pieza/",_1er_escenario, name="1er"),
    path("casa1/",_2do_escenario_1, name="2do_1"),
    path("casa2/",_2do_escenario_2, name="2do_2"),
    path("casa3/",_2do_escenario_3, name="2do_3"),
    path("explosion/",explosion, name="explosion"),
]
