from django.db import models

from .managers import AuthorManager

class Author(models.Model):
    name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    nationality = models.CharField("Nacionalidad", max_length=30)
    age = models.PositiveIntegerField(verbose_name="Edad")

    objects = AuthorManager()

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


    def __str__(self):
        return f"{self.name} {self.last_name}"
