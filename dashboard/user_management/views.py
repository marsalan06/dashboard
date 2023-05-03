from django.shortcuts import render, redirect
from .forms import InfluencerForm, BusinessForm
from .models import Influencer, Business
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth


# Create your views here.

def home(request):
    influencers = Influencer.objects.all()
    return render(request, 'home.html', {'influencers': influencers})

def influencer_signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        influencer_form = InfluencerForm(request.POST)
        if user_form.is_valid() and influencer_form.is_valid():
            user = user_form.save()
            influencer = influencer_form.save(commit=False)
            influencer.user = user
            influencer.save()
            return redirect('home')
    else:
        user_form = UserCreationForm()
        influencer_form = InfluencerForm()
    return render(request, 'signup.html', {'user_form': user_form, 'influencer_form': influencer_form})



def business_signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        business_form = BusinessForm(request.POST)
        if user_form.is_valid() and business_form.is_valid():
            user = user_form.save()
            business = business_form.save(commit=False)
            business.user = user
            business.save()
            return redirect('home')
    else:
        user_form = UserCreationForm()
        business_form = BusinessForm()

    return render(request, 'signup.html', {'user_form': user_form, 'business_form': business_form})

def login(request):
    if request.method == 'POST':
        # Handle form submission
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print(user)
            auth.login(request, user)
            return redirect('home')
        else:
            # Authentication failed
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    elif request.user.is_authenticated:
        # User is already logged in
        return redirect('home')
    else:
        # Show login form
        return render(request, 'login.html')
