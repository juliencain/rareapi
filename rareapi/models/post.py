from django.db import models

class Post(models.Model):

    rare_user = models.ForeignKey('rareapi.RareUser', on_delete=models.CASCADE, related_name='rareusers')
    category = models.ForeignKey('rareapi.Category', on_delete=models.CASCADE, related_name='postcategories')
    title = models.CharField(max_length=55)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=150)
    content = models.TextField()
    approved = models.BooleanField(default=True)
