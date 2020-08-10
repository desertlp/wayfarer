from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.home, name="home"), 
    path('about/', views.about, name="about"), 
    path('cities/', views.cities, name="cities"),
    path('city/<int:city_id>/', views.city, name="city"),
    path('city/<int:city_id>/new_post', views.new_post, name="new_post"),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('accounts/signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)