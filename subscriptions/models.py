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
    custid = models.IntegerField(null=True)
    servid = models.IntegerField(null=True)
    servsigneddt = models.DateTimeField(null=True)
    servexpdt = models.DateTimeField(null=True)
    servstatus = models.CharField(max_length=1,null=True)
    servpayid = models.IntegerField(null=True)
    class Meta:
        db_table = 'custsubscription'
        
class CustPayments(models.Model):
    id = models.AutoField(primary_key=True)
    custid = models.IntegerField(null=True)
    servid = models.IntegerField(null=True)
    custsubid = models.IntegerField(null=True)
    paymentmod = models.CharField(max_length=20,null=True)
    paygateway = models.CharField(max_length=40,null=True)
    payamount = models.DecimalField(max_digits=13, decimal_places=2,null=True)
    payreference = models.CharField(max_length=40,null=True)
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