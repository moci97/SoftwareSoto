from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
import pdfkit
from django_pdfkit import PDFView
from persona.models import Persona


# Create your views here.

def index(request):
    return render(request, 'persona/index.html')


def viewlogin(request):
    return render(request, 'persona/login.html')


def validacion_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/login/datos/get_persona/')
        else:
            return render(request, 'persona/login.html', {'error': 'Invalid username and password'})
    return render(request, 'persona/login.html')


def certificado(request):
    personas = request.session['personas_pk']
    print("=====================")
    print(str(personas))
    print("=====================")
    pdfkit.from_file('persona/certificado.html', 'persona/certificado.pdf')
    return render(request, 'persona/certificado.html')


class Certificado(PDFView):
    template_name = "persona/certificado.html"

    def get_context_data(self, **kwargs):
        context = super(Certificado, self).get_context_data(**kwargs)
        context['persona'] = Persona.objects.filter(pk__in=self.request.session['personas_pk'])
        return context


# class Certificados(PDFView):
#     template_name = "persona/certificado.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(Certificados, self).get_context_data(**kwargs)
#         personas = Persona.objects.filter(pk__in=self.request.session['personas_pk']).values('nombre',
#                                                                                              'id_especialidad__id_facultad__nomb_uni')
#         context['persona'] = personas
#         return context


class GetPersonas(TemplateView):
    template_name = "persona/registro.html"

    def get_context_data(self, **kwargs):
        context = super(GetPersonas, self).get_context_data(**kwargs)
        context['persona'] = Persona.objects.all()
        return context

    def post(self, request):
        self.request.session['personas_pk'] = self.request.POST.getlist('persona_pk')
        return HttpResponseRedirect('/certificado/')
