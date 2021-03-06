from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

  
class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_city = models.CharField(blank=True, max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')

    def __str__(self): 
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs): 
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class City(models.Model): 
    name = models.CharField(max_length=100, blank=False)
    latitude = models.DecimalField(blank=True, max_digits=10, decimal_places=6)
    longitude = models.DecimalField(blank=True, max_digits=10, decimal_places=6)
    country = models.CharField(default='USA', max_length=100, blank=False)
    image = models.ImageField(default='default_city.jpg', upload_to='city_pics/')

    def __str__(self): 
        return f"{self.name} id: {self.id}"


class Post(models.Model): 
    title = models.CharField(blank=False, max_length=200)
    body = models.TextField(blank=False, max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default.jpg', upload_to='post_pics/')
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
 