from django.shortcuts import render 
from django.http import request

# Create your views here.
def index(request):
    return render(request , 'index.html')

def LoginSignup(request):
    return render(request , 'examples/LoginSignup.html')

def About(request):
    return render(request , 'examples/About.html')

def contact(request):
    return render(request , 'examples/contact.html')