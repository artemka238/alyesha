from unittest.util import _MAX_LENGTH
from django.db import models
class Review(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField()
    rating = models.IntegerField()
    review = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name}"
# Create your models here.
