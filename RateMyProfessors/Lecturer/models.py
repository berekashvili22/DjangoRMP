from django.db import models
from Account.models import Account
from django.utils import timezone


# Create your models here.

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

class LecturerReview(models.Model):
         lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
         user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
         score = models.IntegerField(null=False, blank=False, verbose_name="All Ratings")
         text = models.TextField(null=False, blank=False)
         date_added = models.DateTimeField(blank=True, null=True, default=timezone.now)
         
         def __str__(self):
                  return f'{self.lecturer} review'
         
         
         
