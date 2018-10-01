from django.db import models

# Create your models here.

class Persona(models.Model):
    id_persona = models.CharField(primary_key=True)
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=15)
    ano_egrd = models.IntegerField
    mes_egrd = models.IntegerField
    dia_egrd = models.IntegerField
    correo = models.CharField(max_length=25)
    cuidad = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=20)
    tipo_persona = models.CharField(max_length=20)
    grado = models.CharField(max_length=10)

    class Meta:
        managed = True

