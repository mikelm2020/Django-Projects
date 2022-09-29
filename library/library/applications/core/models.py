from django.db import models


class Person(models.Model):
    """Model definition for Person."""

    full_name = models.CharField("Nombre completo", max_length=50)
    country = models.CharField("País", max_length=30)
    passport = models.CharField("Pasaporte", max_length=50)
    age = models.PositiveIntegerField(verbose_name="Edad")
    appellative = models.CharField("Apelativo", max_length=10)

    class Meta:
        """Meta definition for Person."""

        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        db_table = "person"
        unique_together = ["country", "appellative"]
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name="allowed_age")
        ]
        abstract = True

    def __str__(self):
        """Unicode representation of Person."""
        return self.full_name

class Employee(Person):
    job = models.CharField("Empleo", max_length=50)