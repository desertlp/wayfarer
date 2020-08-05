from django.shortcuts import render, HttpResponse, redirect
from .models import City, Post, Comment, User, Profile
from .forms import SignUpForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
    # https://docs.djangoproject.com/en/1.11/_modules/django/contrib/auth/decorators/
    # @login_required

# ---------- AUTH OLD CODE ----------

  # def signup(request): 
  #   # http://localhost:8000/accounts/signup
  #   error = None
  #   form = UserCreationForm()
  #   profile_form = UserProfileForm()
  #   context = {
  #     'form': form, 
  #     'profile_form': profile_form,
  #     'error': error,
  #   }
  #   if request.method == 'POST':
  #     form = UserCreationForm(request.POST)
  #     profile_form = UserProfileForm(request.POST)
  #     if form.is_valid() and profile_form.is_valid(): 
  #       user = form.save(commit=False)
  #       profile = profile_form.save(commit=False)
  #         # dont commit bc need to merge user and profile 
  #       profile.user = user
  #       profile.user.save()
  #       login(request, user)
  #       return redirect('cities')
  #     else:
  #           context = {
  #             'form': form, 
  #             'profile_form': profile_form,
  #             'error': error,
  #           }
  #           return render(request, 'registration/signup.html', context)
  #   else: 
  #     return render(request, 'registration/signup.html', context)

  #   # ========================================

# ---------- AUTH NEW CODE ---------
def signup(request):
    error = None
    if request.method == 'POST':
      form = SignUpForm(request.POST)
        # replaced the user creation form
      if form.is_valid():
          user = form.save()
          user.refresh_from_db()
            # load the profile instance created by the signal
            # refresh why? we have a synchronism issue here. It is easily solved by calling the user.refresh_from_db() method
            # This will cause a hard refresh from the database, which will retrieve the profile instance.
          username = form.cleaned_data.get('username')
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(username=username, password=raw_password)
          user.save()
          raw_password = form.cleaned_data.get('password')
          user = authenticate(username=user.username, password=raw_password)
          login(request, user)
          return redirect('cities')
            # this is per kenny's request, but negates sprint 1 requirement
    else:
      form = SignUpForm()
      return render(request, 'registration/signup.html', {'form': form})
 
# @login_required
def profile(request): 
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
  return render(request, 'profile/profile.html', context)









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

