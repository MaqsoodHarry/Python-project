from django.db import models

# Create your models here.

class service(models.Model):
    model_icon = models.CharField(max_length=20)
    model_title = models.CharField(max_length=20)
    description = models.TextField()
