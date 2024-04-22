from django.shortcuts import render
from django.contrib import messages



username = "praseesh"
password = "pras123"
def login(request):
    return render(request, "login.html")

def display(request):
    uname = request.GET["t1"]
    pwd = request.GET["t2"]
    if uname == username and pwd == password:
        return render(request,"home.html")
    else:
        msg = "Invalid login details"
        return render(request, "login.html", {"message":msg})
    