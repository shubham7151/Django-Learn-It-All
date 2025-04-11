from django.db import models

# Create your models here.

class Student(models.Model):
    std_id = models.CharField(max_length=10)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
