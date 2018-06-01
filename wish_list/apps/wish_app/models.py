from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "User: {}".format(self.username)


class Wish(models.Model):
    items = models.CharField(max_length=255)
    # items = models.ForeignKey(User, related_name="usersitem")
    uploader = models.ForeignKey(User, related_name="uploader")
    date_added = models.DateTimeField(auto_now_add = True)
    share_wish = models.ManyToManyField(User, related_name="share_wish")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "User: {}".format(self.username)
