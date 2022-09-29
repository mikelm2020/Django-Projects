from django.db import models
from django.db.models import Count, Avg, Sum
from django.db.models.functions import Lower


class LoanManager(models.Manager):
    def books_average_ages(self):
        result = self.filter(book__id="2").aggregate(
            average_age=Avg("reader__age"), sum_age=Sum("reader__age")
        )
        return result

    def number_of_borrowed_books(self):
        result = self.values("book").annotate(
            borrow_number=Count("book"), book_title=Lower("book__title")
        )
        for r in result:
            print("*" * 20)
            print(r, r["borrow_number"])
        return result
