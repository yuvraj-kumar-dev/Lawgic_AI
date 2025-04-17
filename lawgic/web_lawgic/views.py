from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comments
from django.views import generic
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    return render(request, "web_lawgic/index.html")

def feature(request):
    return render(request, "web_lawgic/feature.html")

def work(request):
    return render(request, "web_lawgic/workflow.html")

def contact(request):
    return render(request, "web_lawgic/contact.html")

def submit(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = f"{name} {email} {message}"
        with open('C:/Users/yuvra/OneDrive/Desktop/lawgic_ai/lawgic/web_lawgic/contact.txt', 'a') as f:
            f.write(f"{contact} \n")
     return render(request, "web_lawgic/contact.html")

class postList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'web_lawgic\community.html'
    context_object_name = 'posts'

def post_detail(request, slug):
    queryset = Comments.objects.filter(active=1).order_by('-created_on')
    template_name = 'web_lawgic\post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None  
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'queryset' : queryset,})

def chatbot(request):
    return render(request, "web_lawgic/chatbot.html")


