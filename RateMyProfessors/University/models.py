from django.db import models
from Account.models import Account
from django.utils import timezone


# Create your models here.

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

class UniReview(models.Model):
         university = models.ForeignKey(University, on_delete=models.CASCADE)
         user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
         score = models.IntegerField(null=False, blank=False)
         text = models.TextField(null=False, blank=False)
         date_added = models.DateTimeField(blank=True, null=True, default=timezone.now)
         
         def __str__(self):
                  return f'{self.university} review'
         
         
         
