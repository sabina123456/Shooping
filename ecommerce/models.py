from django.db import models

# Create your models here.
class userinfo(models.Model):
    name = models.TextField()
    username = models.TextField(default=None)
    password = models.TextField(default=None)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    utype = models.CharField(max_length=20)

class product(models.Model):
        
    product_id = models.TextField(default=None)
    product_name = models.TextField(default=None)
    category = models.TextField(default=None)
    price = models.BigIntegerField(default=None)
    quantity = models.TextField(default=None)
    image = models.ImageField(default=None)
    warranty = models.TextField(default=None)
    Description = models.TextField(default=None)

class abouts(models.Model):
    cdesc = models.TextField(default=None)
    sdesc = models.TextField(default=None)
    tname = models.TextField(default=None)
    tphoto = models.ImageField(default=None)
    services = models.TextField(default=None)

class Home(models.Model):
    contact = models.TextField(default=None)
    aproduct = models.TextField(default=None)
    address = models.TextField(default=None)
    price = models.TextField(default=None)
    offer = models.TextField(default=None)
    hname = models.TextField(default=None)
    
    

