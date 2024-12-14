from django.db import models
from .category import Category

class Post(models.Model):
    rare_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rareusers')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='postcategories')
    title = models.CharField(max_length=55)
    publication_date = models.DateField()
    image_url = models.DateField()
    content = models.DateField()
    approved = True
