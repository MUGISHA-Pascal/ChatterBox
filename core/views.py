from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import UserCreationform

def front_page(request):
    return render(request,"core/frontpage.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("front_page")
    else:
        form = UserCreationform()
    return render(request,"core/signup.html",{"form":form})