from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length =255)
    password = models.CharField(max_length = 255)
    hired_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Wish(models.Model):
    item = models.CharField(max_length = 255)
    add_by = models.DateField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploder = models.ForeignKey(User, related_name = "user_uplod")
    owner = models.ManyToManyField(User, related_name = "owner_wish")