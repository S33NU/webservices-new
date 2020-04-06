from django.db import models

# Create your models here.


class InvestmentProfile(models.Model):
        investmentId = models.AutoField(primary_key=True)    
        userName = models.CharField(max_length=150)
        investmentAmount = models.CharField(max_length=100)
        investmentType = models.CharField(max_length=100)
        investmentFrequency = models.CharField(max_length=100)
        investmentReviewFrequency = models.CharField(max_length=100)
        montlyAvgSavings = models.CharField(max_length=100)
        lossPercent = models.CharField(max_length=100)
        
       
class InvestmentQuestions(models.Model):
        id = models.AutoField(primary_key=True)
        investqname = models.CharField(max_length=125)
        investqtype = models.CharField(max_length=10)
        investqorder = models.IntegerField()
        investqstatus = models.CharField(max_length=1)
        investqkey = models.CharField(max_length=125)
        investqselection = models.CharField(max_length=100)
        investqcreateddt = models.DateTimeField()  
        investqupdateddt = models.DateTimeField()