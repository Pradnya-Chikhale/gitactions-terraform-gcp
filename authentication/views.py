
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        
        myuser = User.objects.create_user(fname, lname)                                                                                                           
        myuser.fname = fname
        myuser.lname = lname


        myuser.save()
        messages.success(request, "all ok")

        return redirect('signin')


    
    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        
        user = authenticate(fname=fname , lname=lname)

        if user is not None:
            login(request, user)
            fname = user.fname
            return render(request, "authentication/index.html", {'fname : fname'})
        else:
            return redirect('home')
        
    return render(request, "authentication/signin.html")

def signout(request):
    return render(request, "authentication/signout.html")