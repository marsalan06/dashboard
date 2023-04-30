from django.shortcuts import render, redirect
from .forms import InfluencerForm
from .models import Influencer
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth


# Create your views here.

def home(request):
    influencers = Influencer.objects.all()
    return render(request, 'home.html', {'influencers': influencers})

def signup(request):
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

def login(request):
    print("======entryerooooo=====")
    if request.method == 'POST':
        print('======possspppot======')
        # Handle form submission
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print("==============user befor loeging")
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
        print("==============testing login=-----")
        # Show login form
        return render(request, 'login.html')
