from django.db import models

# Create your models here.
class Registration(models.Model):
    clientid = models.AutoField(primary_key=True)
    phonenumber = models.CharField(max_length=100)
    password = models.CharField(max_length=125)
    ip_address = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    email_otp = models.CharField(max_length=25)

class CustRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    custid = models.IntegerField(null=True)
    motp = models.CharField(max_length=10,null=True)
    eotp = models.CharField(max_length=10,null=True)
    ipaddress = models.CharField(max_length=20,null=True)
    device = models.CharField(max_length=60,null=True)
    location = models.CharField(max_length=60,null=True)
    password = models.CharField(max_length=40,null=True)
    createddt = models.DateTimeField(null=True)
    updateddt = models.DateTimeField(null=True)
    class Meta:
        db_table='custregistration'