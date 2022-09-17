from django.db import models
from applications.author.models import Author


class Category(models.Model):
    name = models.CharField("Categoría", max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Categoría"
    )
    authors = models.ManyToManyField(Author, verbose_name="Autor")
    title = models.CharField("Titulo", max_length=50)
    release_date = models.DateField("Fecha lanzamiento")
    front_page = models.ImageField("Portada", upload_to="front_page")
    visits = models.PositiveIntegerField(verbose_name="Visitas")

    def __str__(self):
        return self.title
