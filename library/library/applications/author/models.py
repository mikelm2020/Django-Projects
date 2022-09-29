from django.db import models

from .managers import AuthorManager


class Person(models.Model):
    name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    nationality = models.CharField("Nacionalidad", max_length=30)
    age = models.PositiveIntegerField(verbose_name="Edad", default=18)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Author(Person):
    pseudonym = models.CharField("Pseudonimo", max_length=50, blank=True)

    objects = AuthorManager()

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
