from django.db import models
from django.db.models import Count, Avg, Sum


class LoanManager(models.Manager):
    def books_average_ages(self):
        result = self.filter(book__id="2").aggregate(
            average_age=Avg("reader__age"), sum_age=Sum("reader__age")
        )
        return result
