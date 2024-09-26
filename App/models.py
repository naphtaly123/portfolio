from django.db import models

# Create your models here.
class Message(models.Model):
    email = models.CharField(max_length=250)
    phone = models.IntegerField
    message = models.CharField(max_length=250)