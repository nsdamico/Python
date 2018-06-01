# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request, "login/index.html")

def register(request):
    error = False
    if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
        messages.error(request, "First and Last name must be 2 or more characters")
        error = True
    if not request.POST['first_name'].isalpha() or not request.POST['last_name'].isalpha():
        messages.error(request, "First and Last name must be 2 or more characters")
        error = True
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request, "Email is invalid")
        error = True
    if len(request.POST['password']) < 8:
        messages.error(request, "Password too short")
        error = True
    if request.POST['password'] != request.POST['confirm_password']:
        messages.error(request, "Passwords don't match")
        error = True

    if error:
        return redirect('/')    
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], password = hashed_pw, email = request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/success')  
    
def login(request):
    the_user_list = User.objects.filter(email = request.POST['email'])
    if len(the_user_list) > 0:
        the_user = the_user_list[0]
    else:
        messages.error(request, "Email or password incorrect")
        return redirect('/')
    if bcrypt.checkpw(request.POST['password'].encode(), the_user.password.encode()):
        print "matched"
        request.session['user_id'] = the_user.id
        return redirect('/success')
    else:
        messages.error(request, "Email or password incorrect")
        return redirect('/')
    return redirect('/')

def success(request):
    if not 'user_id' in request.session:
        print "you are not logged in"
        return redirect('/')
    else:
        print "hey person"
        return render(request,'login/success.html')

def logout(request):
    request.session.flush()
    return redirect('/')

    return redirect('/')
