from django.contrib import admin
from django.urls import path

from server.views import Test, Login, Register


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('test/', Test.as_view(), name="test"),

    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register")
]
