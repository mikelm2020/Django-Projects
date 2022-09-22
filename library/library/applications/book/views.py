from django.shortcuts import render
from django.views.generic import ListView

from .models import Book



class BooksListView(ListView):
    
    context_object_name = 'books_list'
    template_name = "book/books_list.html"

    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')

        return Book.objects.find_books(key_word)
    




