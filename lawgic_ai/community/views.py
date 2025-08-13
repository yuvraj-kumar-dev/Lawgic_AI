from django.shortcuts import render
from django.

# Create your views here.

def home(request):
    return render(request, 'home.html')


