from django.db import models

class CountryModel(models.Model):
    class Meta:
        db_table = 'country'
    name = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    area = models.FloatField()
    population = models.IntegerField()


