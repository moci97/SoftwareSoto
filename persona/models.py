from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.CharField(max_length=10)
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=10)

class Universidad(models.Model):
    id_universidad = models.CharField(max_length=10)
    nomb_facultad = models.CharField(max_length=50, null=True, blank=True)

class Facultad(models.Model):
    id_facultad = models.CharField(max_length=10)
    nomb_uni = models.CharField(max_length=50, null=True, blank=True)
    id_universidad = models.ForeignKey(Universidad,on_delete=models.CASCADE, null=True, blank=True)

class Especialidad(models.Model):
    id_esp = models.CharField(max_length=10)
    nombre_esp = models.CharField(max_length=50, null=True, blank=True)
    id_facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE, null=True, blank=True)

class Grado(models.Model):
    id_grado = models.CharField(max_length=10)
    nombre_grado = models.CharField(max_length=50, null=True, blank=True)

class TipoPersona(models.Model):
    id_tipo = models.CharField(max_length=10)
    nombre_tipo = models.CharField(max_length=45, null=True, blank=True)


class Persona(models.Model):
    id_persona = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True)
    fecha = models.DateField( null=True, blank=True)
    correo = models.EmailField(max_length=25, unique=True)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True, blank=True)
    id_tipo = models.ForeignKey(TipoPersona, on_delete=models.CASCADE, null=True, blank=True)
    id_grado = models.ForeignKey(Grado, on_delete=models.CASCADE, null=True, blank=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

