from django.db import models

class Display(models.Model):
    FIrst_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    EmailId=models.CharField(max_length=50)
    Mobile=models.IntegerField()
    Skills=models.CharField(max_length=50)
    Experience=models.IntegerField(max_length=15)
    Salary=models.IntegerField()
    Company=models.CharField(max_length=50)
