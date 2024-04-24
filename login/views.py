# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate

    
# def login_user(request):
#     if 'username' in request.session:
#         return redirect(home)
    
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             request.session['username'] = username
#             return redirect(home)
#         else:
#             message =  "Please enter valid credentials"
#             return render(request,'login.html', {'message':message})
#     return render(request, 'login.html')

# def home(request):
#     if 'username' in  request.session:
#         return render(request, 'home.html')
#     else:
#         return redirect(login_user)
    
# def logout_user(request):
#     if 'username' in request.session:
#         request.session.flush()
#     return redirect(login_user)
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_user(request):
    if 'username' in request.session:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return redirect('home')
        else:
            message = "Please enter valid credentials"
            return render(request, 'login.html', {'message': message})
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

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        if User.objects.filter(username=username).exists():
            msg = "Username already taken"
            return render(request, 'signup.html',{'msg':msg})
        
        user = User.objects.create_user(username=username, password=password,email=email)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # login(request, user)   
            return redirect('login_user')

        else:
            return render(request, 'signup.html', {'error_message': 'Failed to create user.'})
    
    return render(request, 'signup.html')
        