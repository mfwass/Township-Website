from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


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
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)

    @classmethod
    def get(cls):
        latest_banner = SiteBanner.objects.latest('date').content

        if latest_banner is None:
            return None
        else:
            return latest_banner

