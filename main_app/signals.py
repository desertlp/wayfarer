from django.db.models.signals import post_save
    # signal is fired after a user is created that will automatically created a profile for each new user without us having to go in and do this through admin
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
# https://docs.djangoproject.com/en/3.0/topics/signals/
# check this page out, might need to do some more trouble shooting 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()