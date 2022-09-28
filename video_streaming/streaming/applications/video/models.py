from django.db import models
from applications.core.models import FilmGenre, Classification, Country, Provider

class Video(models.Model):
    """Model definition for the streaming's material."""

    VIDEO_TYPE_CHOICES = (
        ("S", "Serie"),
        ("M", "Pelicula"),
        ("D", "Documental"),
        ("R", "Reality"),
    )

    name = models.CharField("Nombre", max_length=200)
    num_year = models.IntegerField(verbose_name="Año")
    active = models.BooleanField(verbose_name="Activo", default=True)
    video_type = models.CharField("Tipo", max_length=1, choices=VIDEO_TYPE_CHOICES)
    film_genre = models.ManyToManyField(
        FilmGenre, verbose_name="Genero Cinematográfico"
    )
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE, verbose_name="Clasificación"
    )
    country = models.ManyToManyField(Country, verbose_name="Pais")
    provider = models.ManyToManyField(Provider, verbose_name="Proveedor")
    duration = models.IntegerField(verbose_name="Duración", blank=True)

    class Meta:

        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return "%s" % self.name