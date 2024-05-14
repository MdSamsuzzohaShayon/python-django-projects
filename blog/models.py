from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Using Django's built-in User model for authors

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title