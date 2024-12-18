from django.db import models

class RareUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    profile_image_url = models.CharField(max_length=150)
    email = models.CharField(max_length=50)
    created_on = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    is_staff =  models.BooleanField(default=True)
    uid = models.CharField(max_length=50)
