from django.db import models
from authentication.models import Account


class BlogPost(models.Model):
    author = models.ForeignKey(Account)

    title = models.TextField(max_length=100)
    content = models.TextField(max_length=2000)

   # image = stuff;

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.title)

