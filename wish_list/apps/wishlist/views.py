from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import datetime
from django.db.models import Q
import bcrypt

def index(request):

    return render(request, 'wishlist/index.html')

def process(request, action):
    if action == "reg":
        error = False
        if len(request.POST['name'])< 3:
            messages.error(request, "Name at least 3 character!")
            error = True
            print "haha"
        if len(request.POST['username'])< 3:
            messages.error(request, "Username at least 3 character!")
            error = True
            print "username"
        if len(request.POST['password']) < 1:
            messages.error(request, "Password at least 1 character!")
            error = True
        if request.POST['confirm_pw'] != request.POST['password']:
            messages.error(request, "Confirm password must the same with your password!")
            error = True
        if len(request.POST['hired_date']) <= 0:
            messages.error(request, "You must choose Hire Date!")
            error = True
        if error:
            return redirect('/main')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(name= request.POST['name'], username = request.POST['username'], password = hashed_pw, hired_date = request.POST['hired_date'])
            request.session['user_id'] = user.id
            return redirect('/dashboard')
    if action == "log":
        try:
            the_user = User.objects.get(username = request.POST['username'])
        except:
            messages.error(request, "Username or Password is incorrect!")
            return redirect('/main')
        if bcrypt.checkpw(request.POST['password'].encode(), the_user.password.encode()):
            request.session['user_id'] = the_user.id
            print "match"
            return redirect('/dashboard')
        else:
            messages.error(request, "Username or password is wrong!")
            return redirect('/main')


def wishes(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        context = {
            'name':user.username,
            'wishes': Wish.objects.filter(Q(uploder=user)| Q(owner=user)).distinct(),
            'other_wishes':Wish.objects.exclude(uploder=user).exclude(owner= user).order_by('add_by'),
        }
        return render(request, 'wishlist/list.html', context)
    if not 'user_id' in request.session:
        print "you are not login"
        return redirect('/main')
def create(request):

    return render(request, 'wishlist/add.html')

def add_process(request): 
    if 'user_id' in request.session:
        error = False
        the_user = User.objects.get(id = request.session['user_id']) 
        if len(request.POST['item']) <= 0:
            messages.error(request, "Item or Product cannot empty!")
            error = True
        elif len(request.POST['item']) <= 3:
                messages.error(request, "Item or Product should be more than 3 characters!")
                error = True        
        if error:
            return redirect('/wish_items/create')
        else:
            wish = Wish.objects.create(item = request.POST['item'], uploder = the_user)
            wish.owner.add(the_user)
            request.session['wish_id'] = wish.id
            print "create"
            return redirect('/dashboard')

def join_wish(request, wish_id):
    if 'user_id' in request.session:
        the_user = User.objects.get(id = request.session['user_id']) 
        wish = Wish.objects.get(id=wish_id)
        wish.owner.add(the_user)
    return redirect('/dashboard')
def remove(request, wish_id):
    if 'user_id' in request.session:
        the_user = User.objects.get(id = request.session['user_id']) 
        wish = Wish.objects.get(id=wish_id)
        the_user.owner_wish.remove(wish)
    return redirect('/dashboard')


def delete(request, wish_id):
    if 'user_id' in request.session:
        the_user = User.objects.get(id = request.session['user_id']) 
        wish = Wish.objects.get(id=wish_id)
        wish.delete()
    return redirect('/dashboard')


def item(request, wish_id):
        wish = Wish.objects.get(id=wish_id)
        uploder = User.objects.get(user_uplod = wish)
        context = {
        'wish': wish,
        'owners': wish.owner.all().exclude(id=uploder.id)
        }
        return render(request, 'wishlist/detail.html', context)    

def logout(request):
    request.session.flush()
    return redirect('/main')