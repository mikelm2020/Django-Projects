from django.db import models

from applications.book.models import Book


class Reader(models.Model):
    name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    nationality = models.CharField("Nacionalidad", max_length=30)
    age = models.PositiveIntegerField(verbose_name="Edad", default=18)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="Lector")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Libro")
    loan_date = models.DateField(verbose_name="Fecha prestámo")
    return_date = models.DateField(
        verbose_name="Fecha devolución", blank=True, null=True
    )
    returned = models.BooleanField(verbose_name="Devuelto")

    def __str__(self):
        return self.book.title
