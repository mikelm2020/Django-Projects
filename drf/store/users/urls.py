# Django
from django.urls import path

# Local
from . import views

app_name='users_app'

urlpatterns = [
    # Template login
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login'
    ),
    path(
        'api/google-login/',
        views.GoogleLoginView.as_view(),
        name='users-google_login'
    )
]
