from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('books/',views.BooksListView.as_view(), name="books"),
]