from django.db import models

# Create your models here.

'''
class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50,unique=True)
    customerStatus_new = models.CharField(max_length=1)
    customerStatus_old = models.CharField(max_length=1)
    profileStatus = models.CharField(max_length=50)
    subscriptionType = models.CharField(max_length=50)
    subscriptionExpirationDate = models.DateTimeField(blank=True,null=True)
    amountPaid = models.CharField(max_length=40)
'''  
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    custregmobile = models.CharField(max_length=15,null=True,unique=True)
    custemail = models.CharField(max_length=100,null=True,unique=True)
    custfirstname = models.CharField(max_length=60,null=True)
    custlastname = models.CharField(max_length=60,null=True)
    custmiddlename = models.CharField(max_length=60,null=True)
    custmaritalstatus = models.CharField(max_length=10,null=True)
    custagegroup = models.CharField(max_length=20,null=True)
    custcountrycode = models.CharField(max_length=4,null=True)
    custadd1 = models.CharField(max_length=100,null=True)
    custadd2 = models.CharField(max_length=100,null=True)
    custcity = models.CharField(max_length=100,null=True)
    custstate = models.CharField(max_length=100,null=True)
    custoccupation = models.CharField(max_length=60,null=True)
    custstatus = models.CharField(max_length=1,null=True)
    custstatusold = models.CharField(max_length=1,null=True)
    zipcode = models.CharField(max_length=12)
    createddt = models.DateTimeField(null=True)
    updateddt = models.DateTimeField(null=True)
    class Meta:
        db_table = 'customer'

class CustTask(models.Model):
    id =  models.AutoField(primary_key=True)
    custid = models.IntegerField()
    taskname = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    tasktype = models.CharField(max_length=1)
    class Meta:
        db_table = 'custtask'