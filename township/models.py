from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

NEWS_POST_CATEGORIES = (
    ('updates', 'Updates'),
    ('elections', 'Elections')
)


class NewsPost(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    content = RichTextField()
    category = models.CharField(max_length=30, choices=NEWS_POST_CATEGORIES)


class SiteBanner(models.Model):
    content = models.TextField()

