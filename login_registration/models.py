from django.db import models

class LoginRegistration(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salt = models.BinaryField()
