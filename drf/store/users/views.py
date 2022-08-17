from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from firebase_admin import auth


from django.shortcuts import render


# Django import
from django.views.generic import TemplateView

# Serializers
from .serializers import LoginSocialSerializer

from .models import User


class LoginUser(TemplateView):
    template_name = "users/login.html"


class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_token = serializer.data.get("token_id")

        decoded_token = auth.verify_id_token(id_token)

        email = decoded_token["email"]
        name = decoded_token["name"]
        avatar = decoded_token["picture"]
        verified = decoded_token["email_verified"]

        user_new, created = User.objects.get_or_create(
            email=email, defaults={"full_name": name, "email": email, "is_active": True}
        )

        if created:
            token = Token.objects.create(user=user_new)
        else:
            token = Token.objects.get(user=user_new)

        userGet = {
            "id": user_new.pk,
            "email": user_new.email,
            "full_name": user_new.full_name,
            "genero": user_new.genero,
            "date_birth": user_new.date_birth,
            "city": user_new.city,
        }
        return Response({"token": token.key, "user": userGet})
