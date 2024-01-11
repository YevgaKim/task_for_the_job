from django.db import models


# Create your models here.
class footballplayer(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    shirtnumber = models.PositiveIntegerField(null=True)