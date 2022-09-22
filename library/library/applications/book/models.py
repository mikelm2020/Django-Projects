from django.db import models
from applications.author.models import Author

from .managers import BookManager


class Category(models.Model):
    name = models.CharField("Categoría", max_length=30)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Categoría"
    )
    authors = models.ManyToManyField(Author, verbose_name="Autor")
    title = models.CharField("Titulo", max_length=100)
    release_date = models.DateField("Fecha lanzamiento")
    front_page = models.ImageField("Portada", upload_to="front_page")
    visits = models.PositiveIntegerField(verbose_name="Visitas")

    objects = BookManager()

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.title
