from django.shortcuts import render
from django.views.generic import ListView

from .models import Author



class AuthorListView(ListView):
    
    context_object_name = 'authors_list'
    template_name = "author/authors_list.html"

    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')

        return Author.objects.find_author_gt(key_word)



