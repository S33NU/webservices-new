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