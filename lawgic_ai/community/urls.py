from django.urls import path
from community import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logoutuser")
]