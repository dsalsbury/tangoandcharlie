from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    current_location = models.CharField(max_length=100, blank=True)
    current_job = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=4, blank=True)
    miscellaneous = models.TextField()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
