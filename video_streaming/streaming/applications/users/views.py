from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm, VerificationForm
from .models import User
from .functions import code_generator


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):
        # We generate the code
        code = code_generator()

        user_obj = User.objects.create_user(
            form.cleaned_data["email"],
            form.cleaned_data["initial_password"],
            full_name=form.cleaned_data["full_name"],
            age=form.cleaned_data["age"],
            code_register=code,
        )

        # Send the code to user's email
        subject = "Confirmación de Email"
        message = f"Código de verificación {code}"
        email_sender = "miguelal@tecnott.com.mx"

        send_mail(
            subject,
            message,
            email_sender,
            [
                form.cleaned_data["email"],
            ],
        )

        # Redirect to confirmation's screen

        return HttpResponseRedirect(
            reverse("users_app:user_verification", kwargs={"pk": user_obj.id})
        )


class LoginUser(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("core_app:user_panel")

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )
        login(self.request, user)

        return super(LoginUser, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("users_app:user_login"))


class UpdatePassword(LoginRequiredMixin, FormView):
    template_name = "users/update.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy("users_app:user_login")
    login_url = reverse_lazy("users_app:user_login")

    def form_valid(self, form):

        actual_user = self.request.user
        user = authenticate(
            email=actual_user.email,
            password=form.cleaned_data["actual_password"],
        )

        if user:
            new_password = form.cleaned_data["new_password"]
            print(new_password)
            actual_user.set_password(new_password)
            actual_user.save()

        logout(self.request)
        return super(UpdatePassword, self).form_valid(form)


class CodeVerificationView(FormView):

    template_name = "users/verification.html"
    form_class = VerificationForm
    success_url = reverse_lazy("users_app:user_login")

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update(
            {
                "pk": self.kwargs["pk"],
            }
        )
        return kwargs

    def form_valid(self, form):
        User.objects.filter(id=self.kwargs["pk"]).update(is_active=True)

        return super(CodeVerificationView, self).form_valid(form)

