from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import User, Trip
import bcrypt

def main(request):
    request.session["logged_in"] = False
    return render(request, "travelbuddy/main.html")

def reg_process(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
        for key, error in errors.iteritems():
            messages.error(request, error)
        return redirect(main)
    else:
        hashed = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())

        user = User.objects.create(name=request.POST["name"], username=request.POST["username"], password=hashed)

        request.session["user_id"] = user.id
        request.session["logged_in"] = True
        return redirect(travels)

def log_process(request):
    errors = User.objects.log_validator(request.POST)
    if len(errors):
        for key, error in errors.iteritems():
            messages.error(request, error)
        return redirect(main)
    else:
        request.session["user_id"] = User.objects.get(username=request.POST["log_username"]).id
        request.session["logged_in"] = True
        return redirect(travels)

def travels(request):
    if request.session["logged_in"] == False:
        return HttpResponse("You must be logged in to view this page")
    else:
        context = {
            "user" : User.objects.get(id=request.session["user_id"]),
            "user_id" : request.session["user_id"],
            "user_trips" : Trip.objects.filter(users__id=request.session["user_id"]),
            "misc_trips" : Trip.objects.exclude(users__id=request.session["user_id"]),
        }
        return render(request, "travelbuddy/travels.html", context)

def add_trip(request):
    if request.session["logged_in"] == False:
        return HttpResponse("You must be logged in to view this page")
    else:
        return render(request, "travelbuddy/add_trip.html")

def trip_process(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors):
        for key, error in errors.iteritems():
            messages.error(request, error)
        return redirect(add_trip)
    else:
        user_logged = User.objects.get(id=request.session["user_id"])
        trip = Trip.objects.create(user=user_logged, locale_name=request.POST["destination"], description=request.POST["description"], date_from=request.POST["datefrom"], date_to=request.POST["dateto"])
        trip.users.add(user_logged)
        return redirect(travels)

def join_process(request, loc_id):
    user = User.objects.get(id=request.session["user_id"])
    trip = Trip.objects.get(id=loc_id)
    trip.users.add(user)
    return redirect(travels)

def destination(request, dest_id):
    if request.session["logged_in"] == False:
        return HttpResponse("You must be logged in to view this page")
    else:
        dest_name = Trip.objects.get(id=dest_id).locale_name
        trip_planner = Trip.objects.all().filter(locale_name=dest_name).values_list("users__name", flat=True)[0]

        context = {
            "trip_planner" : trip_planner,
            "trips" : Trip.objects.get(id=dest_id),
            "all_trips" : Trip.objects.filter(id=dest_id).exclude(user__id=request.session["user_id"]),
            "dest_id" : dest_id,
        }
        return render(request, "travelbuddy/destination.html", context)

def logout(request):
    for key in request.session.keys():
        del request.session[key]
        return redirect(main)

def harddel(request):
    User.objects.all().delete()
    Trip.objects.all().delete()
    return redirect(main)
