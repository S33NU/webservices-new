from django.db import models

# Create your models here.
class Subscription(models.Model):
    subscriptionId = models.AutoField(primary_key=True)
    subscriptionKey = models.CharField(max_length=255)
    subscriptionName = models.CharField(max_length=255)
    subscriptionDescription = models.CharField(max_length=255)
    subscriptionCost = models.CharField(max_length=255)
    subscriptionPeriod = models.CharField(max_length=255)