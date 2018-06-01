# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    alias = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "<User: {}>".format(self.alias)

class Artist(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Record(models.Model):
    title = models.CharField(max_length = 255)
    artist = models.ForeignKey(Artist, related_name ="records")
    genre = models.CharField(max_length = 255)
    year = models.IntegerField()
    uploader = models.ForeignKey(User, related_name = "user_uploads")
    likes = models.ManyToManyField(User, related_name = "user_likes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
