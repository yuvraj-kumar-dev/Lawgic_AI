from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("feature", views.feature, name="feature"),
    path("work", views.work, name="work"),
    path("contact", views.contact, name="contact"),
    path("submit", views.submit, name="submit"),
    path("community/", views.postList.as_view(), name="community"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("chatbot", views.chatbot, name="chatbot"),
]