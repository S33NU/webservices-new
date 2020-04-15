from django.db import models

# Create your models here.


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