from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Address, Counter #<- Sender

# This function will automatically create a counter for an address when it's created:
# 1) The signal is sent by the Address (sender) when it's saved (address_save).
# It includes certain arguments (sender, instance, etc.)
# 2) The create_counter receiver receives the signal and processes it.

@receiver(post_save, sender=Address)
def create_counter(sender, instance, created, **kwargs):
    if created:
        Counter.objects.create(addressId=instance)
    
#REMEMBER: These signals have to be imported to the 'apps.py' file of the app.