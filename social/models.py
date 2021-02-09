from django.db import models

# Create your models here.

class Social_Platform(models.Model):
    platform_name = models.TextField()
    platform_id = models.TextField()

class Social_User(models.Model):
    user_id = models.TextField(primary_key=True)
    user_name = models.TextField()
    platform = models.TextField()
    email = models.TextField(null=True)
