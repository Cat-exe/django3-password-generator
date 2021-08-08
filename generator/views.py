from django.shortcuts import render
from django.http import HttpResponse #This is necessary to get our text to display on the site.
# Use random library to create random password
import random


# Create your views here. These are linked to the urlpatterns list in urls.py
def home(request):
    # return HttpResponse("Hello there, fren :3 ")
    # We will use render instead of HttpResponse for html files.
    return render(request, "generator/home.html") #This already knows to look inside the templates folder.
    #Pass dictionary password key and actual password value as a third parameter.


# def eggs(request):
#     return HttpResponse("<h1>Soft-boiled, hard-boiled, scrambled, or sunny side up?</h1>")

def password(request):
    
    characters = list("abcdefghijklmnopqrstuvwxyz")
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list("abcdefghijklmnopqrstuvwxyz".upper()))
    if request.GET.get('numbers'):
        characters.extend(list("0123456789"))
    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*~"))
    
    
    thepassword = ""

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {'password':thepassword})


def about(request):

    return render(request, "generator/about.html")