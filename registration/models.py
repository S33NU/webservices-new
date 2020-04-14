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
    custid = models.IntegerField()
    motp = models.CharField(max_length=10)
    eotp = models.CharField(max_length=10)
    ipaddress = models.CharField(max_length=20)
    device = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    password = models.CharField(max_length=40)
    createddt = models.DateTimeField()
    updateddt = models.DateTimeField()
    class Meta:
        db_table='custregistration'