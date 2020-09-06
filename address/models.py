from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from .validators import validate_url
from .utils import get_short_code

# Create your models here.

class Address(models.Model):
    address = models.TextField(validators=[validate_url])
    short = models.CharField(max_length=settings.MAX_LENGTH, unique=True, blank=True)

    def __str__(self): #Also called 'magic' methods or 'special' methods. It's what is shown when it's queried.
        return self.address
    
    #This is used to return the URL to the detail of the successfully CREATED post.
    def get_absolute_url(self):
        return reverse('address-detail', kwargs={'pk': self.pk}) #pk for the url parameter
    
    # We overwrite the 'save' method to assign a short-code before it is saved.
    # COMMENTED JUST FOR DEPLOYMENT. (AWS Lambda function could do the work).
    def save(self, *args, **kwargs):
        if not self.short:
            self.short = get_short_code(settings.MAX_LENGTH, self)
        super().save(*args, **kwargs) #That is the method that would have ran to save anyway.
    

class Counter(models.Model):
    visits = models.IntegerField(default=0)
    addressId = models.ForeignKey(Address, on_delete=models.CASCADE)
    
   