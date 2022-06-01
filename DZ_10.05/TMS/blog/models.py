import datetime

from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Post(models.Model):        
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=1200)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, related_name='author_post', on_delete=models.CASCADE) # default='user.email'
    likes = models.ManyToManyField(CustomUser, related_name='author_likes')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
