from operator import truediv
from django.db import models

# Create your models here.
class URLs(models.Model):
    shortURL = models.CharField(max_length=8)
    longURL = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)