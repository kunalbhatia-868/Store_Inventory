from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Box(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    length=models.DecimalField(max_digits=14, decimal_places=3)
    breadth=models.DecimalField(max_digits=14, decimal_places=3)
    height=models.DecimalField(max_digits=14, decimal_places=3)
    area=models.DecimalField(max_digits=14, decimal_places=3,default=0)
    volume=models.DecimalField(max_digits=14, decimal_places=3,default=0)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    
    def calculate_area(self):
        l=self.length
        b=self.breadth
        h=self.height
        return 2 *(l*b + b*h + l*h)
    

    def calculate_volume(self):
        l=self.length
        b=self.breadth
        h=self.height
        return (l*b*h)
    
    def save(self, *args, **kwargs):
        self.area=self.calculate_area()
        self.volume=self.calculate_volume()
        super().save(*args, **kwargs)