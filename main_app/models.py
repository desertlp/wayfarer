from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model): 
    name = models.CharField(max_length=100, blank=False)
    latitude = models.DecimalField(blank=True, max_digits=10, decimal_places=6)
    longitude = models.DecimalField(blank=True, max_digits=10, decimal_places=6)
    img_url = models.URLField(blank=False)

    def __str__(self): 
        return f"{self.name} id: {self.id}"

class Profile(models.Model): 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    home_city = models.CharField(max_length=100)
    country = models.CharField(default="USA", max_length=150)
    profile_img = models.URLField(blank=False)

    def __str__(self): 
        return f"{self.user.username} profile_id: {self.id} user_id: {self.user.id}"

class Post(models.Model): 
    title = models.CharField(blank=False, max_length=100)
    body = models.TextField(blank=False, max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.title

class Comment(models.Model):
    body = models.TextField(blank=False, max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.body
