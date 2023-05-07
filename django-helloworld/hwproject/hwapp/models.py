from django.db import models

# Create your models here.
class Phrases(models.Model):
    firstword = models.CharField(max_length=30)
    secondword = models.CharField(max_length=30)
