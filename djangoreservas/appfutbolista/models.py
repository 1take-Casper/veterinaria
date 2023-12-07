from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dueño(models.Model):
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    nombres = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    motivo_de_visita = models.CharField(max_length=200)

    def apellidos(self):
        return "{} {}".format(self.apellido_paterno,self.apellido_materno)
    
    def __str__(self):
        return self.apellidos()

    class Meta:
        verbose_name='Dueño'
        verbose_name_plural='Dueños'
        db_table='dueño'
        ordering=['apellido_paterno','-apellido_materno']

class Mascota(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    dueño = models.ForeignKey(Dueño, null=True, blank=True, on_delete=models.CASCADE)

class ReservaHora(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    hora = models.IntegerField(choices=[(i, f"{i}:00") for i in range(8, 24)])
    reservado = models.BooleanField(default=False)
    



