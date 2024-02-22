from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    # sign up
    path('register/', views.MySignUpView.as_view(), name='signup'),
    # login
    path('login/', views.MyLoginView.as_view(), name='login'),
    # logout
    path('logout/', LogoutView.as_view(next_page='accounts:login') ,name='logout'),
    #change password
    
    # reset password
    # access denied page
    path('access-denied/', views.AccessDeniedView.as_view(), name='access-denied'),
]