from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Booking(models.Model):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )
    customer = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(999999)])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone_number = models.IntegerField(validators=[MinValueValidator(00000000), MaxValueValidator(99999999)])
    address = models.CharField(max_length=255)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_status = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20)
    payment_date = models.DateField(null=True, blank=True)
    payment_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    service = models.TextField()