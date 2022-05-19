from django.db import models

# Create your models here.
class Listings(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    number_of_bedrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    #image = models.ImageField()

    def __str__(self) -> str:
        return self.title