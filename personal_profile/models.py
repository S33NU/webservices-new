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


class ProfQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    profqname = models.CharField(max_length=125)
    profqtype = models.CharField(max_length=10)
    profqorder = models.IntegerField()
    profqstatus = models.CharField(max_length=1)
    profqkey = models.CharField(max_length=125)
    profqselection = models.CharField(max_length=100)
    profqcreateddt = models.DateTimeField()  
    profqupdateddt = models.DateTimeField()