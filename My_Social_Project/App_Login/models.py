from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    dob = models.DateField(blank=True, null=True)

    website = models.URLField(blank=True)

    facebook = models.URLField(blank=True)



class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    # kake follow korse
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    # kokhon follow korese
    date_created = models.DateTimeField(auto_now_add=True)
