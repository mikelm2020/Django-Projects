from django.db import models
from django.db.models.signals import post_delete

from applications.book.models import Book
from applications.author.models import Person
from .managers import LoanManager
from .signals import update_book_stock


class Reader(Person):
    class Meta:
        verbose_name = "Lector"
        verbose_name_plural = "Lectores"


class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="Lector")
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, verbose_name="Libro", related_name="book_loan"
    )
    loan_date = models.DateField(verbose_name="Fecha prestámo")
    return_date = models.DateField(
        verbose_name="Fecha devolución", blank=True, null=True
    )
    returned = models.BooleanField(verbose_name="Devuelto")

    objects = LoanManager()

    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos"

    def save(self, *args, **kwargs):

        self.book.stock = self.book.stock - 1
        self.book.save()

        return super(Loan, self).save(*args, **kwargs)

    def __str__(self):
        return self.book.title


post_delete.connect(update_book_stock, sender=Loan)
