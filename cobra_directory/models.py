from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=100, blank=True, default="NA")
    last_name = models.CharField(max_length=100, blank=True, default="NA")
    current_location = models.CharField(max_length=200, blank=True, default="NA")
    current_job = models.CharField(max_length=300, blank=True, default="NA")
    year = models.CharField(max_length=4, blank=True, default="NA")
    miscellaneous = models.TextField(blank=True, default="NA")
    
    def __unicode__(self):
        return self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u, first_name=u.email)[0])
