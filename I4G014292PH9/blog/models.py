from turtle import title
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=23)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title