from django.shortcuts import render, HttpResponse, redirect
from .models import City, Post, Comment, User, Profile
from .forms import SignUpForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm, PostForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# @login_required
def profile(request): 
    posts = Post.objects.filter(user=request.user)
    print(posts)
    context = {
        'posts': posts
    }
    return render(request, 'profile/profile.html', context)

# @login_required
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
    return redirect('city', city_id=2)
    # return redirect('city', city_id=3)


def city(request, city_id): 
    side_bar_cities = City.objects.all().order_by('name')
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city_id=city_id).order_by('-updated')
    context = {
        'city': city,
        'posts': posts,
        'side_bar_cities': side_bar_cities,
    }
    print(posts)
    return render(request, 'city/show.html', context)
    # return HttpResponse('cities')


# @login_required
# this should go on a city_id page 
def new_post(request, city_id):
    if request.method == 'POST':
        submitted_new_post_form = PostForm(request.POST, request.FILES)
        if submitted_new_post_form.is_valid():
            post = submitted_new_post_form.save(commit=False)
            post.user_id = request.user.id
            post.city_id = city_id
            post.save()
            return redirect('post', post.id)
    else: 
        new_post_form = PostForm()
        return render(request, 'post/new.html', {'form': new_post_form})

# @login_required
def post(request, post_id): 
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'post/show.html', context)
    # return HttpResponse('post show page')


# ---------------- EDIT AND DELETE ONLY YOUR STUFF ----------------

def edit_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id) 
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post', post.id)
    else: 
        post = Post.objects.get(id=post_id) 
        form = PostForm(instance=post)
    context = {
    'form': form,
    }
    return render(request, 'post/edit.html', {'form': form})

    # @login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id).delete()
    return redirect('cities')



# ---------------- EDIT AND DELETE ALL ----------------
#SPRINT 3
    # # @login_required
    # def edit_post(request, post_id):
    #     post = Post.objects.get(id=post_id) 
    #     form = PostForm(instance=post)
    #     if request.method == 'POST' and request.user == post.user:
    #         post = Post.objects.get(id=post_id) 
    #         form = PostForm(request.POST, request.FILES, instance=post)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('post', post.id)
    #     elif request.user != post.user:
    #         return HttpResponse('you cant edit this sucker')
    #     else: 
    #         if request.user == post.user:
    #             post = Post.objects.get(id=post_id) 
    #             form = PostForm(instance=post)
    #     context = {
    #         'form': form,
    #     }
    #     return render(request, 'post/edit.html', {'form': form})

    # # @login_required
    # def delete_post(request, post_id):
    #     post = Post.objects.get(id=post_id)
    #     if request.user == post.user:
    #         post = Post.objects.get(id=post_id).delete()
    #         return redirect('cities')
    #         # return HttpResponse(f"deleted post: {post_id}")
    #     else:
    #         return HttpResponse('you cant deleted this mfffff***')


