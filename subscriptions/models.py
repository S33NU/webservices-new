from django.db import models

# Create your models here.
class Subscription(models.Model):
    subscriptionId = models.AutoField(primary_key=True)
    subscriptionKey = models.CharField(max_length=255)
    subscriptionName = models.CharField(max_length=255)
    subscriptionDescription = models.CharField(max_length=255)
    subscriptionCost = models.CharField(max_length=255)
    subscriptionPeriod = models.CharField(max_length=255)
    
    
class CustSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    custid = models.IntegerField()
    servid = models.IntegerField()
    servsigneddt = models.DateTimeField()
    servexpdt = models.DateTimeField()
    servstatus = models.CharField(max_length=1)
    servpayid = models.IntegerField()
    class Meta:
        db_table = 'custsubscription'
        
class CustPayments(models.Model):
    id = models.AutoField(primary_key=True)
    custid = models.IntegerField()
    servid = models.IntegerField()
    custsubid = models.IntegerField()
    paymentmod = models.CharField(max_length=20)
    paygateway = models.CharField(max_length=40)
    payamount = models.DecimalField(max_digits=13, decimal_places=2)
    payreference = models.CharField(max_length=40)
    class Meta:
        db_table = 'custpayments'
        
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    sername = models.CharField(max_length=100)
    serdesc = models.CharField(max_length=512)
    serstatus = models.CharField(max_length=1)
    sercreateddt = models.DateTimeField()
    serupdateddt =  models.DateTimeField()
    class Meta:
        db_table = 'service'

class ServicePrice(models.Model):
    id = models.AutoField(primary_key=True)
    serid =  models.IntegerField()
    serprice = models.DecimalField(max_digits=10, decimal_places=2)
    sermode = models.CharField(max_length=40)
    sercreateddt = models.DateTimeField()
    serupdateddt = models.DateTimeField()
    serstatus = models.CharField(max_length=1)
    class Meta:
        db_table = 'serviceprice'