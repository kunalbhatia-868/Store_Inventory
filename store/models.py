from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Box(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    length=models.DecimalField(max_digits=14, decimal_places=3)
    bredth=models.DecimalField(max_digits=14, decimal_places=3)
    height=models.DecimalField(max_digits=14, decimal_places=3)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    
    @property
    def area(self):
        l=self.length
        b=self.bredth
        h=self.height
        return 2 *(l*b + b*h + l*h)
    
    @property
    def volume(self):
        l=self.length
        b=self.bredth
        h=self.height
        return (l*b*h)
    