from django.urls import path 
from . import views

urlpatterns = [
    # Home
    path('', views.home, name="home"), 
    # About 
    path('about/', views.about, name="about"), 
        # Render a blank template
    # City Index
    path('cities/', views.cities, name="cities"),
    path('post/<int:post_id>/', views.post, name='post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
        # city.posts
        # event listener to display a city to the right on click? 
    # Add Post Page
        # City automatically applied
    # Post Show Page
    # Sign Up
    path('accounts/signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
]