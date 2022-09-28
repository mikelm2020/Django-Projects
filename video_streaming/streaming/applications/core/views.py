import datetime
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"
    login_url = reverse_lazy("users_app:user_login")
