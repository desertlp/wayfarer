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
    path('city/<int:city_id>/', views.city, name="city"),
    path('city/<int:city_id>/new_post', views.new_post, name="new_post"),
    
    path('post/new/', views.new_post, name='new_post'),
        # this path should be from the city page 

    path('post/<int:post_id>/', views.post, name='post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),

    path('accounts/signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
]