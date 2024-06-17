from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    product = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    inventory = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999)])
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999)])
