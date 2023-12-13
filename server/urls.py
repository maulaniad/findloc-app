from django.contrib import admin
from django.urls import path

from server.views import Test


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('test/', Test.as_view(), name="test")
]
