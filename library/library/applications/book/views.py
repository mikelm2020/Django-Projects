import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book


class BooksListView(ListView):

    context_object_name = "books_list"
    template_name = "book/books_list.html"

    def get_queryset(self):
        key_word = self.request.GET.get("kword", "")
        initial_date = self.request.GET.get("initial_date", "")
        final_date = self.request.GET.get("final_date", "")

        if initial_date and final_date:
            return Book.objects.find_books_with_date(
                key_word,
                datetime.datetime.strptime(initial_date, "%Y-%m-%d").date(),
                datetime.datetime.strptime(final_date, "%Y-%m-%d").date(),
            )
        else:
            return Book.objects.find_books(key_word)


class BooksByCategoryListView(ListView):

    context_object_name = "books_list"
    template_name = "book/books_by_category_list.html"

    def get_queryset(self):

        return Book.objects.list_books_by_category(2)


class BookDetailView(DetailView):
    model = Book
    template_name = "book/detail.html"
