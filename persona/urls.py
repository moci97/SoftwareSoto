
from django.urls import path
from persona.views import index
urlpatterns = [
    path('', index),
]