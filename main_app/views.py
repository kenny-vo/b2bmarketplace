"""App views are here"""


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django_tables2 import RequestConfig

from .forms import ListingForm, LoginForm, SignUpForm
from .models import Listing

def index(request):
    """Show all objects"""

    listings = Listing.objects.all().order_by('-date')
    form = ListingForm()
    return render(request, 'index.html', {'listings': listings, 'form':form})

def register(request):
    """Register new users"""

    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def detail(request, listing_id):
    """"Get detail of one listing"""
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'detail.html', {'listing': listing})

def update_listing(request, pk, template_name='request_form.html'):
    """Update a listing"""

    listing = get_object_or_404(Listing, pk=pk)
    form = ListingForm(request.POST or None, instance=listing)
    if form.is_valid():
        form.save()
        messages.success(request, 'Request has been updated.')
        return redirect('/')
    return render(request, template_name, {'form': form})

def delete_listing(request, pk, template_name='listing_confirm_delete.html'):
    """Delete a listing"""

    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        listing.delete()
        messages.error(request, 'Request deleted.')
        return redirect('/')
    return render(request, template_name, {'object': listing})

def post_listing(request, template_name='request_form.html'):
    """Create a new Listing"""

    form = ListingForm(request.POST)
    if form.is_valid():
        listing = form.save(commit=False)
        listing.user = request.user
        listing.save()
        messages.success(request, 'New request posted.')
        return redirect('/')
    return render(request, template_name, {'form': form})

def profile(request, username):
    """Go to a user's profile"""

    user = User.objects.get(username=username)
    listings = Listing.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'listings': listings})

def request_form(request):
    """Go to the request form"""

    return render(request, 'request_form.html')

def login_view(request):
    """Go to login"""

    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/")# Redirect to a success page.
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """Logout"""

    logout(request)
    return HttpResponseRedirect('/')

def listing_list(request):
    """Table view"""

    return render(request, 'listing_list.html', {'table': Listing.objects.all()})
