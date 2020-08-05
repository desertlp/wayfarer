from django.shortcuts import render, HttpResponse, redirect
from .models import City, Profile, Post, Comment, User
# from django.contrib.auth.forms import UserCreationForm
  # idk if this is the deal but I think it will work
from .forms import UserCreationForm, UserProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
    # https://docs.djangoproject.com/en/1.11/_modules/django/contrib/auth/decorators/
    # @login_required

# Create your views here.

# ---------- AUTH ----------

def signup(request): 
  # http://localhost:8000/accounts/signup
  error = None
  form = UserCreationForm()
  profile_form = UserProfileForm ()
  context = {
    'form': form, 
    'profile_form': profile_form,
    'error': error,
  }
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    profile_form = UserProfileForm(request.POST)


    if form.is_valid() and profile_form.is_valid(): 
      user = form.save()
      profile = profile_form.save(commit=False)
        # dont commit bc need to merge user and profile 
      profile.user = user
      profile.save()
      login(request, user)
      return redirect('cities')
    else:
          return render(request, 'registration/signup.html', context)
          return render(request, 'registration/signup.html', {'form': form, 'error': form.errors})
  else: 
    return render(request, 'registration/signup.html', context)




def profile(request): 
  # http://localhost:8000/profile/
  # user = User.objects.filter()
  profile = Profile.objects.all()
  user = User.objects.all()
  context = {
    'profile': profile,
    'user': user,
  }
  return render(request, 'profile/profile.html', context)
  # return HttpResponse('profile page, profile and user model')
















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

