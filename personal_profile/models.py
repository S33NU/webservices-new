from django.db import models


class CustPersonalProfile(models.Model):
    id = models.AutoField(primary_key=True)
    custid =  models.IntegerField(null=True)
    order = models.IntegerField()
    attribute = models.CharField(max_length=125,null=True)
    custresponse = models.CharField(max_length=100,null=True)
    attributetype = models.CharField(max_length=1,null=True)
    createddt = models.DateTimeField()
    class Meta:
        db_table = 'custpersonalprofile'