from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 60)
    email = models.EmailField(max_length = 90, unique=True)
    address = models.CharField(max_length= 80)
    image = models.ImageField(upload_to='photos' , default='default.jpg')
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created']
