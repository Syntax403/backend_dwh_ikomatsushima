from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class Activity(models.Model):
    ESTADO_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    portada = models.ImageField(upload_to='activities_flyers/', null=True, blank=True)  # Flayer del evento
    titulo = models.CharField(max_length=255)
    fecha_evento = models.DateField()  # Solo fecha, sin la hora
    fecha_termino = models.DateField()  # Fecha de término
    ubicacion = models.CharField(max_length=255)
    descripcion_breve = models.TextField(max_length=500)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actividades')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='borrador')

    class Meta:
        ordering = ['-fecha_publicacion']  # Ordena por fecha de publicación descendente

    def clean(self):
        """Verifica que el autor sea un Admin o un Gestor de Actividades."""
        if self.autor.role != 'admin' and self.autor.sub_role != 'gestor_actividades':
            raise ValidationError("Solo los administradores y los gestores de actividades pueden crear actividades.")

    def save(self, *args, **kwargs):
        """Ejecuta la validación antes de guardar."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
