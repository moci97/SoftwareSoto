from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
import pdfkit
from django_pdfkit import PDFView
from persona.models import Persona, Universidad, Facultad, Especialidad, TipoPersona,Grado


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
    pdfkit.from_file('persona/certificado.html', 'persona/certificado.pdf')
    return render(request, 'persona/certificado.html')


class Certificado(PDFView):
    template_name = "persona/certificado.html"

    def get_context_data(self, **kwargs):
        context = super(Certificado, self).get_context_data(**kwargs)
        context['persona'] = Persona.objects.filter(pk__in=self.request.session['personas_pk'])
        context['universidad'] = Universidad.objects.filter(pk__in=self.request.session['universidad_pk'])
        context['facultad'] = Facultad.objects.filter(pk__in=self.request.session['facultad_pk'])
        context['especialidad'] = Especialidad.objects.filter(pk__in=self.request.session['especialidad_pk'])
        context['grado'] = Grado.objects.filter(pk__in=self.request.session['grado_pk'])

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
        context['universidad'] = Universidad.objects.all()
        context['facultad'] = Facultad.objects.all()
        context['especialidad'] = Especialidad.objects.all()
        context['tipo_persona'] = TipoPersona.objects.all()
        context['grado'] = Grado.objects.all()
        return context

    def post(self, request):
        self.request.session['personas_pk'] = self.request.POST.getlist('persona_pk')
        self.request.session['universidad_pk'] = self.request.POST['universidad_pk']
        self.request.session['facultad_pk'] = self.request.POST.getlist('facultad_pk')
        self.request.session['especialidad_pk'] = self.request.POST.getlist('especialidad_pk')
        self.request.session['grado_pk'] = self.request.POST.getlist('grado_pk')
        return HttpResponseRedirect('/certificado/')

