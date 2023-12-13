from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=75)

    class Meta:
        db_table = "USER"
