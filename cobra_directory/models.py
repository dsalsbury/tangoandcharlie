from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    current_location = models.CharField(max_length=200, blank=True, default="??")
    current_job = models.CharField(max_length=300, blank=True, default="??")
    year = models.CharField(max_length=4, blank=True, default="0000")
    major = models.CharField(max_length=300, blank=True, default="??")
    
    def __unicode__(self):
        return self.current_location

