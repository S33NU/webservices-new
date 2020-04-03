from django.db import models

# Create your models here.
class LookUpMaster(models.Model):
    id = models.AutoField(primary_key=True)
    lookupid = models.IntegerField()
    lookupmasterid = models.IntegerField()
    lookupname = models.CharField(max_length=125)
    lookupparam1 = models.CharField(max_length=10)
    lookupparam2 = models.CharField(max_length=10)
    lookupstatus = models.CharField(max_length=1)
    lookupcreateddt = models.DateField()  
    lookupupdateddt = models.DateField() 
     