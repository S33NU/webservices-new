from django.db import models

# Create your models here.

        
       
        
class CustInvestmentProfile(models.Model):
        id = models.AutoField(primary_key=True)
        custid = models.IntegerField()
        order = models.IntegerField()
        attribute = models.CharField(max_length=125,null=True)
        custresponse = models.CharField(max_length=100,null=True)
        attributetype = models.CharField(max_length=1,null=True)
        createddt = models.DateTimeField()
        class Meta:
                db_table = 'custinvestmentprofile'