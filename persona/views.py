from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from persona.forms import PersonaForm
from persona.models import Persona
# Create your views here.

def index(request):
    return render(request,'persona/index.html' )

def viewlogin(request):
    return render(request,'persona/login.html')


def validacion_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            persona = Persona.objects.all()
            contexto = {'persona': persona}
            return render(request, 'persona/registro.html', contexto)

        else:
            return render(request, 'persona/login.html', {'error': 'Invalid username and password'})
    return render(request, 'persona/login.html')

def certificado(request, id):
    return render (request, 'persona/certificado.html')






