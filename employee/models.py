from django.db import models

# Create your models here.

class Employee(models.Model):
    eId = models.CharField(max_length=10)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    