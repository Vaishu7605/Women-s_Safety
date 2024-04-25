from django.db import models




 
class clients(models.Model):
    First_Name = models.CharField( max_length=50)
    Last_Name  = models.CharField (max_length=50, blank=True )
    E_mail = models.EmailField (max_length=50) 
    Create_Password =models.CharField (max_length=8 )
    Confirm_password =models.CharField (max_length=8 )
    

class Feedback(models.Model):
    uname=models.CharField(max_length=50)
    mail=models.EmailField()
    query=models.TextField()


   


# Create your models here.
