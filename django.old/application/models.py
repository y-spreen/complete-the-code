from django.db import models

# Create your models here.

class LinkModel(models.Model):
    status = models.IntegerField(default=0)
    number = models.IntegerField()
