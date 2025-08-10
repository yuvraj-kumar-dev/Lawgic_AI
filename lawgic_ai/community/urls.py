from django.urls import path
from community import views

urlpatterns = [
    path("", views.home, name="home")
]