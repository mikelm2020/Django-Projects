from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(forms.ModelForm):

    initial_password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Contraseña"}),
    )
    confirm_password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Repetir Contraseña"}),
    )

    class Meta:
        model = User
        fields = ("email", "full_name", "age")

    def clean_confirm_password(self):
        if (
            self.cleaned_data["initial_password"]
            != self.cleaned_data["confirm_password"]
        ):
            self.add_error("confirm_password", "Las contraseñas no son iguales")
        else:
            if len(self.cleaned_data["initial_password"]) < 5:
                self.add_error(
                    "initial_password",
                    "La contraseña debe tener por lo menos 5 caracteres",
                )


class LoginForm(forms.Form):

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Contraseña"}),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Los datos del usuario no son correctos")

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    actual_password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Contraseña actual"}),
    )
    new_password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Contraseña nueva"}),
    )


class VerificationForm(forms.Form):
    code_register = forms.CharField(required=True)

    def __init__(self, pk, *args, **kwargs):
        self.user_id = pk
        super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_code_register(self):
        code = self.cleaned_data["code_register"]

        if len(code) == 6:
            # We verificate if the code and the id are valid
            active = User.objects.code_validation(self.user_id, code)
            if not active:
                raise forms.ValidationError("El código es incorrecto")
        else:
            raise forms.ValidationError("El código es incorrecto")
