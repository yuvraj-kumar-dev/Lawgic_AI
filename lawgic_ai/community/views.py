from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    
    else:
        return redirect('login_user')


def login_user(request):
    
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('home')
        
        else:

            return render(request, 'login.html')
    
    return render(request, 'login.html')


def logout_user(request):

    logout(request)

    return render(request, 'home.html')

def signup_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists!!")
    
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login_user')

    return render(request, 'signup.html')



