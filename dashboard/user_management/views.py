from django.shortcuts import render, redirect
from .forms import InfluencerForm, BusinessForm
from .models import Influencer, Business
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    influencers = Influencer.objects.all()
    return render(request, 'home.html', {'influencers': influencers})


def user_registration(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
       
        if user_form.is_valid():
            user = user_form.save()
            return redirect('home')
        else:
            print("========error====")
    else:
        user_form = UserCreationForm()
    return render(request, 'user_reg.html', {'user_form': user_form})


@login_required(login_url='/login/')
def influencer_signup(request):
    
    if request.method == 'POST':
        influencer_form = InfluencerForm(request.POST, user=request.user)
        
        if influencer_form.is_valid():
            influencer = influencer_form.save(commit=False)
            influencer.user = request.user
            influencer.save()
            return redirect('home')
        else:
            print(influencer_form.errors)
            print("========error====")
    else:
        influencer_form = InfluencerForm(user=request.user)
    return render(request, 'signup2.html', {'influencer_form': influencer_form})



@login_required(login_url='/login/')
def business_signup(request):

    if request.method == 'POST':
        business_form = BusinessForm(request.POST, user=request.user)
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = request.user
            business.save()
            return redirect('home')
        else:
            print("=======errors----")
            print(business_form.errors)
    else:
        business_form = BusinessForm(user=request.user)

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

@login_required(login_url='/login/')
def business_list(request):
    context = {}
    
    if request.user.first_name and request.user.last_name:
        context['name'] = request.user.first_name + ' ' + request.user.last_name
    else:
        context['name'] = request.user.username
    
    business_list = list(Business.objects.filter(user__id = request.user.id).values('name','contact_no','start_date','end_date','reference_no','report_ready','user__email'))
    
    context['business_list'] = business_list
    return render(request, 'business-list.html' , context)


@login_required(login_url='/login/')
def influencer_list(request):
    context = {}
    
    if request.user.first_name and request.user.last_name:
        context['name'] = request.user.first_name + ' ' + request.user.last_name
    else:
        context['name'] = request.user.username
    
    influencer_list_for_hire = list(Influencer.objects.filter(status='hire').values('id','name','state','city','zip_code','rank','status','user__email'))
    
    context['influencer_list'] = influencer_list_for_hire
    print(request.user.id)
    influencer_list_hired = Influencer.objects.filter(business_association__user_id=request.user.id).exclude(status='hire').values('name','user__email')
    context['influencer_list_hired'] = influencer_list_hired
    print(influencer_list_hired)
    return render(request, 'influencer-list.html' , context)


def change_status(request, id):
    
    influencer_obj = get_object_or_404(Influencer, id=id)

    influencer_obj.status = 'ask_quote'
    influencer_obj.business_association.set([request.user.id])
    influencer_obj.save()
    return redirect('influencer-list')



def logout_view(request):
    logout(request)
    return redirect('home')