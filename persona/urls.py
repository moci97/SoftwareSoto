
from django.urls import path
from persona import views as persona_views
urlpatterns = [
    path('', persona_views.index),
    path('login/', persona_views.viewlogin),
    path('login/datos/', persona_views.validacion_login, name="login"),
    path('login/datos/certificado/<int:id>', persona_views.certificado, name="certificado"),
]