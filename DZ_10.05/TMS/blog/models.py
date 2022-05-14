import datetime

from django.db import models
from django.utils import timezone


class Author(models.Model):
    nickname = models.CharField(max_length=50)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname


class Post(models.Model):        
    post_name = models.CharField(max_length=200)
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)