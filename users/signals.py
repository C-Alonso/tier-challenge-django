from django.db.models.signals import post_save
from django.contrib.auth.models import User #<- Sender
from django.dispatch import receiver
from .models import Profile

# This function will automatically create a profile for a User when it's created:
# 1) The signal is sent by the User (sender) when it's saved (post_save).
# It includes certain arguments (sender, instance, etc.)
# 2) The create_profile receiver receives the signal and processes it.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()

#REMEMBER: These signals have to be imported to the 'apps.py' file of the app.