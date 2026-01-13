# farmers/models.py
from django.db import models

class Farmer(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)

    district = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)
    village = models.CharField(max_length=50)

    land_size = models.DecimalField(max_digits=5, decimal_places=2)
    land_ownership = models.CharField(max_length=50)

    experience = models.TextField(blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
