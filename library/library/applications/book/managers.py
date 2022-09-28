from django.db import models
from django.db.models import Count


class BookManager(models.Manager):
    def find_books(self, kword):
        result = self.filter(
            title__icontains=kword, release_date__range=("2000-01-01", "2002-01-01")
        )

        return result

    def find_books_with_date(self, kword, initial_date, final_date):
        result = self.filter(
            title__icontains=kword, release_date__range=(initial_date, final_date)
        )

        return result

    def list_books_by_category(self, category_param):

        return self.filter(category__id=category_param).order_by("title")

    def add_author_book(self, book_id, author):
        book = self.get(id=book_id)
        book.authors.add(author)
        return book

    def books_number_of_loans(self):
        result = self.aggregate(number_of_loans=Count('book_loan'))
        return result


class CategoryManager(models.Manager):
    def category_by_author(self, author_param):

        return self.filter(category_book__authors__id=author_param).distinct()

    def books_by_category(self):
        result = self.annotate(number_of_books=Count("category_book"))
        for r in result:
            print("*" * 20)
            print(r, r.number_of_books)

        return result
