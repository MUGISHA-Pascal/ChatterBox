from django.shortcuts import render
from .forms import usercreationform

def front_page(request):
    return render(request,"core/frontpage.html")

def signup(request):
    if request.method=="POST":
        form = usercreationform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = usercreationform()
    return render(request,"core/signup.html")