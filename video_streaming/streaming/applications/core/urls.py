from django.urls import path
from . import views

app_name = "core_app"

urlpatterns = [
    path('', views.HomePage.as_view(), name='user_panel'),
]
