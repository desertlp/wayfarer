from django.urls import path 
from . import views

urlpatterns = [
    # Home
    path('', views.home, name="home"), 
    # About 
    path('about/', views.about, name="about"), 
        # Render a blank template
    # City Index
        # Post(s) Loops
            # Post Comments Loop??? 
    # Add Post Page
        # City automatically applied
    # Post Show Page
        # Post Comments Loop
    # Profile
    # Login/SignUp 

]