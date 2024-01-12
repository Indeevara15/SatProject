from django.db import models

# Create your models here.
class SatData(models.Model):

    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    pincode = models.IntegerField()
    sat_score = models.IntegerField()

