from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import AddPost

# Create your views here.

def home(request):
    
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    
    else:
        return render(request, 'home.html')


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

@login_required
def profile(request):

    username = request.user.username

    context = {'username': username}

    return render(request, 'profile.html', context)

class community(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'community.html'

class post(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post.html'

class addpost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddPost
    template_name = 'addpost.html'
    # fields = '__all__'
    success_url = reverse_lazy('community')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





