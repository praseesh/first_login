
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

registered_users = {}

def sign_up(request):
    if 'username' in request.session:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username in registered_users:
            msg = "Username already taken"
            return render(request, 'signup.html', {'msg': msg})
        
        registered_users[username] = password
        
        return render(request, 'login.html')

    return render(request,'signup.html')

def login_user(request):
    if 'username' in request.session:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        if username in registered_users and registered_users[username] == password:
            request.session['username'] = username
            return redirect('home')
        else:
            # return redirect('home')
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def home(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    else:
        return redirect('login_user')
    
def logout_user(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login_user')

