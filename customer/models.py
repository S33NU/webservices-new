from django.db import models

# Create your models here.


class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50,unique=True)
    customerStatus_new = models.CharField(max_length=1)
    customerStatus_old = models.CharField(max_length=1)
    profileStatus = models.CharField(max_length=50)
    subscriptionType = models.CharField(max_length=50)
    subscriptionExpirationDate = models.DateTimeField(blank=True,null=True)
    amountPaid = models.CharField(max_length=40)