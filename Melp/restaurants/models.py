from django.db import models

# Create your models here.

class Restaurant(models.Model):
    id = models.TextField(primary_key=True)
    rating = models.IntegerField()
    name = models.TextField()
    site = models.URLField()
    email = models.EmailField()
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
