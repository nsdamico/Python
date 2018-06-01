# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *

def index(request):
    if 'id' in request.session:
        context = {
            "user" : User.objects.get(id = request.session['id'])
        }
    else: 
        context = {
            "user" : "UNAVAILABLE"
        }
    context["artists"] = Artist.objects.all()
    context["records"] = Artist.objects.all()
    print context
    return render(request, "records/index.html", context)

def register(request):
    user = User.objects.create(alias = request.POST['alias'], password = request.POST['password'])
    request.session['id'] = user.id
    return redirect('/')

def login(request):
    the_user_list = User.objects.filter(alias = request.POST['alias'])
    if len(the_user_list) > 0:
        the_user = the_user_list[0]
        if request.POST['password'] == the_user.password:
            print "hey you have a session"
            reqest.session['id'] = the_user.id
        else:
            print "FAIL" 
            return redirect('/')
    else:
        print "FAIL"
        return redirect('/')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def add_record(request):
    if len(request.POST['new_artist']) < 1:
        artist = Artist.objects.get(id = request.POST['ex_artist'])
    else:
        artist = Artist.objects.create(name = request.POST['new_artist'])
    user = User.objects.get(id = request.session['id'])
    Record = Record.objects.create(title = request.POST['title'], genre = request.POST['genre'], year = request.POST['year'], uploaded = user, artist = artist)
    return redirect('/')

