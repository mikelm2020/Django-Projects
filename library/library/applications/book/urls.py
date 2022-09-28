from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("books/", views.BooksListView.as_view(), name="books"),
    path(
        "books-by-category",
        views.BooksByCategoryListView.as_view(),
        name="books_by_category",
    ),
    path("book-detail/<pk>/", views.BookDetailView.as_view(), name="book_detail"),
]
