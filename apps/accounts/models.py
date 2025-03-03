from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    )

    SUBROLE_CHOICES = (
        ('periodista', 'Periodista'),
        ('gestor_actividades', 'Gestor de Actividades'),
        ('fotografo', 'Fotógrafo'),
        ('', 'Ninguno'),  # Para otros roles
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    sub_role = models.CharField(
        max_length=20, choices=SUBROLE_CHOICES, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        """
        Si el usuario no es Editor, se elimina el sub-role automáticamente.
        """
        if self.role != 'editor':
            self.sub_role = ''
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role} - {self.sub_role})"
