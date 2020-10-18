from django.db import models
from django.utils import timezone


'''
Ambiente -> Entidad del sistema
Clase relacionada -> CD24 [Entity]
'''
class Ambiente(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    aforo = models.IntegerField(default=40)

    def __str__(self):
        return f"{self.nombre}: Sala {self.ubicacion} con un aforo de {self.aforo} personas."


'''
Evento -> Entidad del sistema
Clase relacionada -> CD83 [Entity]
'''
class Evento(models.Model):
    nombre = models.CharField(max_length=80)
    ubicacion = models.CharField(max_length=60)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Evento {self.nombre} con lugar en {self.ubicacion}."


'''
Actividad -> Entidad del sistema
Clase relacionada -> CD01 [Entity]
'''
class Actividad(models.Model):
    nombre = models.CharField(max_length=80)
    tipo = models.CharField(max_length=30)
    evento = models.ForeignKey(Evento,  on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Actividades"

    def __str__(self):
        return f"{self.tipo}: {self.nombre}."


'''
Ponente -> Entidad del sistema
Clase relacionada -> CD73 [Entity]
'''
class Ponente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    especialidad = models.CharField(max_length=30)

    class Meta:
        ordering = ['apellido']

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


'''
Turno -> Entidad del sistema
Clase relacionada -> CD44 [Entity]
'''
class Turno(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=15)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.nombre}"
