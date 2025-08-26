from django.shortcuts import render
# from langchain.community import prompttemplate

# Create your views here.

def chatbot(request):
    return render(request, 'chatbot.html')
