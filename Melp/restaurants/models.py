from django.db import models

# Create your models here.

class Restaurant(models.Model):
    id = models.TextField(primary_key=True)
    rating = models.URLField()
    name = models.TextField()
    site = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
