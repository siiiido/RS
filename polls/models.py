from django.db import models

# Create your models here.
class Polls(models.Model):
    UserCode = models.CharField(max_length=100)