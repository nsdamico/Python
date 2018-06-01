from __future__ import unicode_literals
from django.db import models
import bcrypt
import datetime

class TravelMgr(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 3:
            errors["name"] = "Name must be AT LEAST 3 characters long."
            if len(postData["name"]) < 1:
                errors["name"] = "Name is a MANDATORY field"
        if len(postData["username"]) < 3:
            errors["username"] = "Username must be AT LEAST 3 characters long."
            if len(postData["username"]) < 1:
                errors["username"] = "Username is a MANDATORY field"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be AT LEAST 8 characters long"
        if postData["password"] != postData["confirm_pw"]:
            errors["confirm_pw"] = "Password and Confirm PW does NOT match"
        return errors

    def log_validator(self, postData):
        errors = {}
        if not User.objects.filter(username=postData["log_username"]):
            errors["login"] = "Username or Password invalid. Try again or register account above"
        if User.objects.filter(username=postData["log_username"]):
            if not bcrypt.checkpw(postData["log_pw"].encode(), User.objects.get(username=postData["log_username"]).password.encode()):
                errors["login"] = "Username or Password invalid. Try again or register account above"
        return errors

    def trip_validator(self, postData):
        date_today = datetime.datetime.strptime(str(postData["datefrom"]),"%Y-%m-%d")
        errors = {}
        if len(postData["destination"]) < 1:
            errors["destination"] = "Destination is a MANDATORY field"
        if len(postData["description"]) < 1:
            errors["description"] = "Description is a MANDATORY field"
        if len(postData["datefrom"]) < 1:
            errors["datefrom"] = "Travel Date From is a MANDATORY field"
        if postData["dateto"] < postData["datefrom"]:
            errors["dateto"] = "You can not travel BACK to the FUTURE" 
        if date_today < datetime.datetime.today():
            errors["datefrom"] = "You can not travel BACK to the FUTURE"
        if len(postData["dateto"]) < 1:
            errors["dateto"] = "Travel Date To is a MANDATORY field"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelMgr()

class Trip(models.Model):
    user = models.ForeignKey(User, related_name="planner")
    users = models.ManyToManyField(User,related_name="travelers")
    locale_name = models.CharField(max_length=255)
    description = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelMgr()