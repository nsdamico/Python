# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.Charfield(max_length = 45)
    last_name = models.Charfield(max_length = 45)
    email = models.Charfield(max_length = 255)
    password = models.Charfield(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    first_name = models.Charfield(max_length = 45)
    last_name = models.Charfield(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Book(models.Model):
    title = models.Charfield(max_length = 255)
    isbn = models.Charfield(max_length = 255)
    publisher = models.Charfield(max_length = 255)
    genre = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(Author, related_name = "my_books")
    likes = models.ManyToManyField(User, related_name = "user_likes") 