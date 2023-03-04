from django.db import models
from django.contrib.auth.models import User
class Ngodetails(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=300,unique=True)
    logo=models.ImageField(upload_to='my_img')
    state=models.CharField(max_length=300)
    vision=models.TextField()
    description = models.TextField()
    founding_year=models.IntegerField()
    emailid=models.EmailField()
    phone=models.IntegerField()


class blog_model(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    ngo=models.ForeignKey(Ngodetails,on_delete=models.CASCADE,default=None)
    image1=models.ImageField(upload_to='my_img')
    imge2=models.ImageField(upload_to='my_img')
    title1=models.CharField(max_length=300)
    title2=models.CharField(max_length=300)
    desc=models.TextField()

class achievement(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    ngo=models.ForeignKey(Ngodetails,on_delete=models.CASCADE,default=None)
    img1=models.ImageField(upload_to='my_img')
    img2=models.ImageField(upload_to='my_img')
    t1=models.CharField(max_length=300)
    t2=models.CharField(max_length=300)
    desc2=models.TextField()






class desc_model(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    ngo=models.ForeignKey(Ngodetails,on_delete=models.CASCADE,default=None)
    im1=models.ImageField(upload_to='my_img')
    img2=models.ImageField(upload_to='my_img')
    title1=models.CharField(max_length=300)
    title2=models.CharField(max_length=300)
    desc=models.TextField()

class achievement_model(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    ngo=models.ForeignKey(Ngodetails,on_delete=models.CASCADE,default=None)
    img1=models.ImageField(upload_to='my_img')
    
    t1=models.CharField(max_length=300)
   
    desc2=models.TextField()
