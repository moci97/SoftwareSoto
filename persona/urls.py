from django.urls import path
from persona import views as persona_views
from persona.views import *

urlpatterns = [
    path('', persona_views.index),
    path('login/', persona_views.viewlogin),
    path('login/datos/', persona_views.validacion_login, name="login"),
    path('login/datos/get_persona/', GetPersonas.as_view(), name="get_persona"),
    path('login/datos/certificado/', Certificados.as_view(), name="get_certificado"),

]
