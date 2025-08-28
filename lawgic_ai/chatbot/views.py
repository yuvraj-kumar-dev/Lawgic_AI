from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from langchain_core.prompts import PromptTemplate

# Create your views here.

PROMPT = PromptTemplate(
    """You are a **Professional Legal Adviser** whose task is to give the Best and Verified Legal Advice 
    to the **User** and If you are not sure about any advice then it is best to tell the user to contact
    any legal advisor rather than telling any unverified suggestions"""
)

@login_required
def chatbot(request):
    return render(request, 'chatbot.html')
