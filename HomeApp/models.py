from django.db import models

class StudentRegister(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    age = models.CharField(max_length=400, null=True, blank=True)
    place = models.CharField(max_length=400, null=True, blank=True)
  
   #  def __str__(self):
   #      return self.name