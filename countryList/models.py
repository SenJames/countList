from django.db import models

# Create your models here.

class CountryModel(models.Model):
    country = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_created=True,auto_now=True)
    continent = models.CharField(max_length=200, blank=True)
    iso2= models.CharField(max_length=5, blank=True)
    long= models.IntegerField("")
    lat= models.IntegerField("")

    class Meta:
        ordering = ['created']