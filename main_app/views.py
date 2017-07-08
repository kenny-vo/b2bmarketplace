from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy

from .forms import ListingForm, LoginForm
from .models import Listing


def index(request):
    listings = Listing.objects.all()
    form = ListingForm()
    return render(request, 'index.html', {'listings': listings, 'form':form})

def detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'detail.html', {'listing': listing})

def delete_listing(request, pk, template_name='listing_confirm_delete.html'):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method =='POST':
        listing.delete()
        return redirect('/')
    return render(request, template_name, {'object': listing})

def profile(request, username):
    user = User.objects.get(username=username)
    listings = Listing.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'listings': listings})

def request_form(request):
    return render(request, 'request_form.html')

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
