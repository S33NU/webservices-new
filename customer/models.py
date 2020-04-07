from django.db import models

# Create your models here.


class CustomerDetails(models.Model):
    
    userName = models.CharField(max_length=50,primary_key=True)
    customerStatus = models.CharField(max_length=1)
    profileStatus = models.CharField(max_length=50)
    subscriptionType = models.CharField(max_length=50)
    subscriptionExpirationDate = models.DateTimeField(blank=True,null=True)
    amountPaid = models.CharField(max_length=40)