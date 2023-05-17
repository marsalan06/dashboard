from django.urls import path
from . import views

urlpatterns = [
    path('signup-influencer/', views.influencer_signup, name='influencer-signup'),
    path('signup-business/', views.business_signup, name='business-signup'),
    path('home/',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('user-reg/',views.user_registration,name='user-reg'),
    path('logout/',views.logout_view,name='logout-view'),
    path('business-list/',views.business_list,name='business-list')

]