from django.shortcuts import render, HttpResponse, redirect
from .models import City, Profile, Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
    # https://docs.djangoproject.com/en/1.11/_modules/django/contrib/auth/decorators/
    # @login_required

# Create your views here.

# ---------- AUTH ----------

def signup(request): 
  error = None
    # change this based on if statements and errors that we expect
  form = UserCreationForm()
  context = {
    'form': form, 
    'error': error,
  }
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid(): 
      user = form.save()
      login(request, user)
        # login is a django method, does everythign behind the scenes
        # need to import this method: from django.contrib.auth import login
      return redirect('cities')
    else:
          # global error 'User account already exists' this doesnt work
          return render(request, 'registration/signup.html', context)
          return render(request, 'registration/signup.html', {'form': form, 'error': form.errors})
  else: 
    # aka if it is a get request, we need to send the new user sign up form 
    # import this from django: from django.contrib.auth.forms import UserCreationForm
      # this was created by django, must use the form
    return render(request, 'registration/signup.html', context)

def profile(request): 
  user = User.objects.filter(user=user_id)
  profile = Profile.objects.filter(user=user_id)
  context = {
    'profile': profile,
    'user': user
  }
  # return render(request, 'registration/profile.html', context)
  return HttpResponse('profile page, profile and user model')





# HOME PAGE 
def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def cities(request): 
    cities = City.objects.all()
    context = {
        'cities': cities,
    }
    # return render(request, 'cities.html', context)
    return HttpResponse('cities')

