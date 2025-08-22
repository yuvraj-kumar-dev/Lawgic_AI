from django.urls import path
from community import views
from .views import community, post

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logoutuser"),
    path("signup", views.signup_user, name="signup"),
    path("profile", views.profile, name="profile"),
    path("community", community.as_view() , name="community"),
    path("post/<int:pk>", post.as_view(), name = "post"),
]