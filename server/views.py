import json

from django.shortcuts import redirect
from inertia import render
from django import views
from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
from django.http import HttpRequest, HttpResponse

from server.data.forms import LoginForm, RegisterForm
from server.data.models import User


class Test(views.View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(
            request=request,
            component="Test",
            props={
                'test': {
                    'first_name': "Mameng",
                    'last_name': "Galuh"
                }
            }
        )


class Login(views.View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(
            request=request,
            component="auth/Login"
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = LoginForm(json.loads(request.body))

        if not form.is_valid():
            return render(
                request=request,
                component="auth/Login"
            )

        user_data = User.objects.filter(
            Q(username=form.cleaned_data['username']) | Q(email=form.cleaned_data['username'])
        ).first()

        if not user_data:
            return render(
                request=request,
                component="auth/Login"
            )

        if not check_password(form.cleaned_data['password'], user_data.password):
            return render(
                request=request,
                component="auth/Login"
            )

        return redirect(to="test")


class Register(views.View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(
            request=request,
            component="auth/Register"
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = RegisterForm(json.loads(request.body))

        if not form.is_valid():
            return render(
                request=request,
                component="auth/Register"
            )

        user = User(
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username'],
            fullname=form.cleaned_data['fullname'],
            password=make_password(form.cleaned_data['password'])
        )

        user.save()

        return render(
            request=request,
            component="auth/Login"
        )
