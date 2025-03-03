from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class News(models.Model):
    ESTADO_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    portada = models.ImageField(upload_to='news_portadas/', null=True, blank=True)
    titulo = models.CharField(max_length=255)
    resumen = models.TextField(max_length=500)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noticias')
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='borrador')  # Nuevo campo para el estado

    class Meta:
        ordering = ['-fecha_publicacion']

    def clean(self):
        """Verifica que el autor sea un Admin o periodista antes de guardar."""
        if self.autor.role != 'admin' and self.autor.sub_role != 'periodista':
            raise ValidationError("Solo los administradores y periodistas pueden ser autores de noticias.")

    def save(self, *args, **kwargs):
        """Ejecuta la validación antes de guardar."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
