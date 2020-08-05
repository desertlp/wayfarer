from django.shortcuts import render, HttpResponse, redirect
from .models import City, Post, Comment, User, Profile
from .forms import SignUpForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
<<<<<<< HEAD
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register/signup.html', {'form': form})
 
=======
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

>>>>>>> submaster
# @login_required
def profile(request): 
  return render(request, 'profile/profile.html')

def edit_profile(request):
  if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid and pform.is_valid():
              uform.save()
              pform.save()
              return redirect('profile')
  else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)
  context = {
    'uform': uform,
    'pform': pform,
  }
  return render(request, 'profile/edit.html', context)






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

