from atexit import register
from django.contrib import admin

from .models import Author


class AdminAuthor(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "last_name",
        "nationality",
        "age",
    )
    list_filter = ("nationality",)
    search_fields = (
        "name",
        "last_name",
        "nationality",
        "age",
    )
    ordering = ("id",)


admin.site.register(Author, AdminAuthor)
