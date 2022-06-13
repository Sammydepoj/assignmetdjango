from django.db import models
from django.forms import CharField

# Create your models here.
class schools(models.Model):
    name=models.CharField(max_length=23)
    address=models.CharField(max_length=25)
    def _str_(self)-> str:
        return self.name

class country(models.Model):
    address=models.CharField(max_length=23)
    def _str_(self)-> str:
        return self.address
