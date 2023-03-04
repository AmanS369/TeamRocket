from django.db import models
from django.contrib.auth.models import User
class Ngodetails(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=300,unique=True)
    logo=models.ImageField(upload_to='cat_img/')
    state=models.CharField(max_length=300)
    vision=models.TextField()
    description = models.TextField()
    founding_year=models.IntegerField()
    emailid=models.EmailField()
    phone=models.IntegerField()
