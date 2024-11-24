from django.db import models
from django.contrib.auth.models import User  # Si quieres asociar con el usuario

class ProgramaIntercambio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self):
        return self.nombre



class Postulacion(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    programa = models.ForeignKey(ProgramaIntercambio, on_delete=models.CASCADE)
    fecha_postulacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=50,
        choices=[('Pendiente', 'Pendiente'), ('Aceptada', 'Aceptada'), ('Rechazada', 'Rechazada')],
        default='Pendiente'
    )

    def __str__(self):
        return f"{self.estudiante.username} - {self.programa.nombre}"


class DocumentoFamilia(models.Model):
    familia = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    archivo = models.FileField(upload_to='documentos_familias/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Documento de {self.familia.username}"
