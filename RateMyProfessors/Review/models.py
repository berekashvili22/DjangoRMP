from django.db import models
from django.utils import timezone

from Account.models import Account
from University.models import University
from Lecturer.models import Lecturer


class UniReview(models.Model):
         university = models.ForeignKey(University, on_delete=models.CASCADE)
         user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
         score = models.IntegerField(null=False, blank=False, verbose_name="All Ratings")
         text = models.TextField(null=False, blank=False)
         date_added = models.DateTimeField(blank=True, null=True, default=timezone.now)
         
         def __str__(self):
                  return f'{self.university} review'
         

class LecturerReview(models.Model):
         lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
         user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
         score = models.IntegerField(null=False, blank=False, verbose_name="All Ratings")
         text = models.TextField(null=False, blank=False)
         date_added = models.DateTimeField(blank=True, null=True, default=timezone.now)
         
         def __str__(self):
                  return f'{self.lecturer} review'
         
                  
