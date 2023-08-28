from django.db import models


# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return self.name
