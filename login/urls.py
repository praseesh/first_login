from django.urls import path
from .views import login_user, home, logout_user, sign_up

urlpatterns = [
    path('', login_user, name='login_user'),
    path('home', home, name='home'),
    path('logout_user', logout_user, name='logout_user'),
    path('signup',sign_up, name="signup" )
]