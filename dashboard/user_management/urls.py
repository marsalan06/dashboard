from django.urls import path
from . import views

urlpatterns = [
    path('signup-influencer/', views.influencer_signup, name='influencer-signup'),
    path('signup-business/', views.business_signup, name='business-signup'),
    path('home/',views.home,name='home'),
    path('login/', views.login, name='login'),

]