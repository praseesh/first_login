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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

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
