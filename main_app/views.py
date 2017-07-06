from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import ListingForm, LoginForm
from .models import Listing

def home(request):
    listings = Listing.objects.all()
    form = ListingForm()
    return render(request, 'home.html', {'listings': listings, 'form':form})

def show(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'show.html', {'listing': listing})

def profile(request, username):
    user = User.objects.get(username=username)
    listings = Listing.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'listings': listings})

def post_listing(request):
    form = ListingForm(request.POST)
    if form.is_valid():
        listing = form.save(commit = False)
        listing.user = request.user
        listing.save()
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request, 'login.html', {'form': form, 'message': "The account has been disabled."})
            else:
                return render(request, 'login.html', {'form': form, 'message': "The username and/or password is incorrect."})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
