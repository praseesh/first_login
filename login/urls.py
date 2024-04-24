from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.login_user),
    path('login', views.home),
    path('signout', views.logout_user)
]
