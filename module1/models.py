from django.db import models
class Register(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    class Meta:
        db_table="Register"

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    subject=models.CharField(max_length=255)
    message=models.CharField(max_length=255)
    class Meta:
        db_table="ContactUs"