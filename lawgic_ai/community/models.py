from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author) + ' | ' + str(self.date)
    
class comment(models.Model):
    author = models.CharField(max_length=255)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add = True)
    body = models.TextField()

    def __str__(self):
        return str(self.author)
    

