from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    user_address = models.TextField(max_length=100)
    user_gender = models.CharField(max_length=100)    
    user_image = models.ImageField(upload_to="image/", null=True)
    phone=models.CharField(max_length=12)
    pincode=models.CharField(max_length=6)

class category(models.Model):
    category_name = models.CharField(max_length=225)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class product_multimage(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,)

    multimage = models.ImageField(upload_to="multi/image",null=True,blank=True)