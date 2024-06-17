from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Staff(models.Model):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999)])
