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
'''    
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    custregmobile = models.CharField(max_length=15,unique=True)
    custemail = models.CharField(max_length=100,unique=True)
    custfirstname = models.CharField(max_length=60)
    custlastname = models.CharField(max_length=60)
    custmiddlename = models.CharField(max_length=60)
    custmaritalstatus = models.CharField(max_length=1)
    custagegroup = models.CharField(max_length=20)
    custcountrycode = models.CharField(max_length=4)
    custadd1 = models.CharField(max_length=100)
    custadd2 = models.CharField(max_length=100)
    custcity = models.CharField(max_length=100)
    custstate = models.CharField(max_length=100)
    custoccupation = models.CharField(max_length=60)
    custstatus = models.CharField(max_length=1)
    custstatusold = models.CharField(max_length=1)
    custprofstatus = models.CharField(max_length=5)
    zipcode = models.Charfield(max_length=12)
    createddt = models.DateTimeField()
    updateddt = models.DateTimeField()
    class Meta:
        db_table = 'customer'
'''        