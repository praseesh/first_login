from django.shortcuts import render, redirect




username = "praseesh"
password = "pras123"
def login(request):
    return render(request, "login.html")

# def display(request):

def display(request):
    uname = request.POST["t1"]
    pwd = request.POST["t2"]
    if uname == username and pwd == password:
        return render(request,"home.html")
    else:
        msg = "Invalid login details"
        return render(request, "login.html", {"message":msg})
# def signout(request):
#     return redirect("login.html")

def signout(request):
    # Perform sign out logic...
    return render(request, 'login.html')
    
    