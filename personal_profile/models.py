from django.db import models

class PersonalProfile(models.Model):
    registeredmobile = models.CharField(max_length=225)
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    age = models.CharField(max_length=225)
    marriedstatus = models.CharField(max_length=225)
    addr1 = models.CharField(max_length=225)
    addr2 = models.CharField(max_length=225)
    addr3 = models.CharField(max_length=225)
    addr4 = models.CharField(max_length=225)
    occupation = models.CharField(max_length=225)


    
class CustPersonalProfile(models.Model):
    id = models.AutoField(primary_key=True)
    custid =  models.IntegerField(null=True)
    order = models.IntegerField(unique=True)
    attribute = models.CharField(max_length=100,null=True)
    custresponse = models.CharField(max_length=100,null=True)
    attributetype = models.CharField(max_length=1,null=True)
    createddt = models.DateTimeField()
    class Meta:
        db_table = 'custpersonalprofile'