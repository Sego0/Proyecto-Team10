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



def _2do_escenario_1(request):

    objectsPrev = request.GET.get('objectPrev', '0000')
    if "0" in objectsPrev:
        return redirect("/AppQuiz/explosion/")

    return render(request, "Casa.html")

def _2do_escenario_2(request):
    return render(request, "Casa.html")    

def _2do_escenario_3(request):
    return render(request, "Casa.html") 

def explosion(request):
    return render(request, "explosion.html")
def loginView(request):
    titulo = 'login'
    form = UsuarioLoginFormulario(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        usuario = authenticate(username=username, password=password)
        login(request, usuario)
        return redirect('inicio')

    context = {
        'form' : form,
        'titulo' : titulo
    }

    return render(request, 'Usuario/login.html', context)

def registro(request):

    titulo = 'Crear una cuenta'
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroFormulario()

    context = {

        'form': form,
        'titulo': titulo

    }

    return render(request, 'Usuario/registro.html', context)

def logout_vista(request):
    logout(request)
    return redirect('/')