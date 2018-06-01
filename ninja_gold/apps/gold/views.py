# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.shortcuts import render, redirect

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'log' in request.session:
        request.session['log'] = []
    return render(request, "gold/index.html")

def process(request, location):
    if location == "farm":
        gold = random.randint(10,20)
        eventStr = ("You stole {} gold from the {}".format(gold, location), "")
    if location == "cave":
        gold = random.randint(5,10)
        eventStr = ("You stole {} gold from the {}".format(gold, location), "")
    if location == "house":
        gold = random.randint(2,5) 
        eventStr = ("You stole {} gold from the {}".format(gold, location), "")
    if location == "casino":
        gold = random.randint(-50,50) 
        if gold >= 0: 
            eventStr = ("You stole {} gold from the {}".format(gold, location),"win")
        else:
            eventStr = ("The {} stole {} gold from you".format(location, gold),"loss")

    request.session['gold'] += gold
    request.session['log'].insert(0, eventStr)
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')