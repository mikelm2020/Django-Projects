from django.contrib import admin

from .models import Book, Category

admin.site.register(Category)


class AdminBook(admin.ModelAdmin):

    list_display = (
        "id",
        "category",
        "title",
        "release_date",
        "visits",
    )
    list_filter = ("category",)
    search_fields = (
        "category",
        "title",
        "release_date",
        "visits",
    )
    ordering = ("id",)
    date_hierarchy = ('release_date')


admin.site.register(Book, AdminBook)
