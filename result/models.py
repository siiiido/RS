from django.db import models

# Create your models here.

class Matching_Table(models.Model):   
    
    user_man_id = models.TextField(null=False, primary_key=True)

    user_woman_id = models.TextField(null=False) 