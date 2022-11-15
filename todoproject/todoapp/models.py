from django.db import models
from datetime import date
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    priority = models.IntegerField()
    date= models.DateTimeField(null=True)

    def __str__(self):
        return self.name
