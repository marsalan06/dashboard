from django.shortcuts import render, redirect
from .forms import InfluencerForm, BusinessForm
from .models import Influencer, Business
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout





# Create your views here.

def home(request):
    influencers = Influencer.objects.all()
    return render(request, 'home.html', {'influencers': influencers})


def user_registration(request):
    if request.method == 'POST':
        print("=======testing me here------")
        user_form = UserCreationForm(request.POST)
        # influencer_form = InfluencerForm(request.POST)
        print("=======aaa=====")
        print(user_form)
        # print(influencer_form)
        if user_form.is_valid():
            user = user_form.save()
            # influencer = influencer_form.save(commit=False)
            # influencer.user = user
            print("======i am here....")
            # influencer.save()
            return redirect('home')
        else:
            print("========error====")
    else:
        user_form = UserCreationForm()
        # influencer_form = InfluencerForm()
    return render(request, 'user_reg.html', {'user_form': user_form})

def influencer_signup(request):
    
    users = User.objects.all()
    
    if request.method == 'POST':
        influencer_form = InfluencerForm(request.POST, users=users)
        print("=======testing me here------")
        # user_form = UserCreationForm(request.POST)
        print("=======aaa=====")
        # print(user_form)
        # print(request.user)
        # print(influencer_form)
        if influencer_form.is_valid():
            print("oooooo")
            user = influencer_form.cleaned_data['user']
            # print(user)
            # user = request.user
            influencer = influencer_form.save(commit=False)
            influencer.user = user
            print("======i am here....")
            influencer.save()
            return redirect('home')
        else:
            print("========error====")
    else:
        # user_form = UserCreationForm()
        influencer_form = InfluencerForm(users=users)
    return render(request, 'signup2.html', {'influencer_form': influencer_form})



@login_required(login_url='/login/')
def business_signup(request):
    # influencer = Influencer.objects.all()
    if request.method == 'POST':
        # user_form = UserCreationForm(request.POST)
        business_form = BusinessForm(request.POST)
        if business_form.is_valid():
            # user = user_form.save()
            business = business_form.save(commit=False)
            business.user = request.user
            business.save()
            return redirect('home')
    else:
        # user_form = UserCreationForm()
        business_form = BusinessForm()

    return render(request, 'signup2.html', {'business_form': business_form})

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
            print("=====login failed=====")
            error_message = 'Invalid username or password.'
            return render(request, 'login_2.html', {'error_message': error_message})
    elif request.user.is_authenticated:
        # User is already logged in
        return redirect('home')
    else:
        # Show login form
        return render(request, 'login_2.html')



def logout_view(request):
    logout(request)
    return redirect('home')