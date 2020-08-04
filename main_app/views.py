from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# HOME PAGE 
def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')