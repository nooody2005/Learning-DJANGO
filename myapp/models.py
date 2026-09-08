from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('myapp:index')
    

    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.DecimalField(max_digits=6,decimal_places=2)
    item_image = models.URLField(max_length=500,default='https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png')
    is_available= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) 


class Category(models.Model):
    name= models.CharField(max_length=100)
    added_on = models.DateField(auto_now=True)
    def __str_(self):
        return self.name