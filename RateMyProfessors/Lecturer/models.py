from django.db import models

class Lecturer(models.Model):
         first_name = models.CharField(max_length=250)
         last_name = models.CharField(max_length=250)
         image = models.ImageField(null=False, upload_to='lecturer_image')
         rating = models.FloatField(null=True, blank=True)
         phone = models.CharField(max_length=100, unique=True, null=True, blank=True)
         email = models.CharField(max_length=150, unique=True, null=True, blank=True)
         website = models.CharField(max_length=200, unique=True, null=True, blank=True)
         about = models.TextField(null=True, blank=True)
         
         def __str__(self):
                  return f'{self.first_name} {self.last_name}' 
