from django.db import models

from genericrouterproject.models import BaseModel


# Create your models here.
class Employee(BaseModel):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    age = models.IntegerField()
    salary = models.FloatField()
    address = models.TextField()

    def __str__(self):
        return self.name