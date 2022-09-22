from django.db import models


class BookManager(models.Manager):
    def find_books(self, kword):
        result = self.filter(
            title__icontains=kword, release_date__range=("2000-01-01", "2002-01-01")
        )

        return result
