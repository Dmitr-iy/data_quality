from django.contrib.auth.models import User
from django.db import models


class ConcentrateQuality(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    iron = models.FloatField()
    silicon = models.FloatField()
    aluminum = models.FloatField()
    calcium = models.FloatField()
    sulfur = models.FloatField()
