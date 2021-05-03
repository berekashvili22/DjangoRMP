from django.db import models

class University(models.Model):
         name = models.CharField(max_length=250, unique=True)
         short_name = models.CharField(max_length=10, unique=True)
         logo = models.ImageField(null=False, upload_to='logos')
         code = models.IntegerField(unique=True)
         rating = models.FloatField(null=True, blank=True)
         address = models.TextField(null=True, blank=True)
         phone = models.CharField(max_length=100, unique=True, null=True, blank=True)
         email = models.CharField(max_length=150, unique=True, null=True, blank=True)
         website = models.CharField(max_length=200, unique=True, null=True, blank=True)
         about = models.TextField(null=True, blank=True)
         
         def __str__(self):
                  return self.short_name
         
