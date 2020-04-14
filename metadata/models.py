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
    lookupcreateddt = models.DateTimeField()  
    lookupupdateddt = models.DateTimeField() 
    class Meta:
        db_table = 'lookupmaster'
    
class MenuItems(models.Model):
    menuItemId = models.AutoField(primary_key=True)
    menuItemName = models.CharField(max_length=100)
    menuItemKey = models.CharField(max_length=100) 
    menuItemLink = models.CharField(max_length=100)
    menuItemState = models.CharField(max_length=50)
    menuItemParent = models.CharField(max_length=100)
    UIIcon = models.CharField(max_length=100)
    class Meta:
        db_table = 'menuitems'
        

class ProfQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    profqname = models.CharField(max_length=125)
    profqclass = models.CharField(max_length=1)
    profqtype = models.CharField(max_length=10)
    profqorder = models.IntegerField()
    profqstatus = models.CharField(max_length=1)
    profqchoicelabels = models.CharField(max_length=125)
    profqcreateddt = models.DateTimeField()  
    profqupdateddt = models.DateTimeField()
    class Meta:
        db_table = 'profquestion'