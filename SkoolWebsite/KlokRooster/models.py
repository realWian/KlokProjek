from django.db import models

# Create your models here.
class Rooster(models.Model):
    naam = models.CharField(max_length=256)
    
    periode1 = models.TimeField()
    periode2 = models.TimeField()
    periode3 = models.TimeField()
    periode4 = models.TimeField()
    pouse1 = models.TimeField()
    periode5 = models.TimeField()
    periode6 = models.TimeField()
    periode7 = models.TimeField()
    periode8 = models.TimeField()
    pouse2 = models.TimeField()
    periode9 = models.TimeField()
    periode10 = models.TimeField()
    periode11 = models.TimeField()
    periode12 = models.TimeField()
    uitkomtyd = models.TimeField()

    def __str__(self):
        return self.naam