from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Listing

def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings': listings})

# def show(request, listing_id):
#     listing = Listing.objects.get(id=listing_id)
#     return render(request, 'show.html', {'listing': listing})
