from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() #Unrestricted
     #auto_now=True <- This would be useful for getting the update time.
    date_posted = models.DateTimeField(default=timezone.now) #NO PARENTHESIS; not executed, just passed.
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Action for if the user that created the post gets deleted.
    #CASCADE deletes the post when it's posting user gets deleted.

    def __str__(self): #Also called 'magic' methods or 'special' methods. It's what is shown when it's queried.
        return self.title
    
    #This is used to return the URL to the detail of the successfully CREATED post.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) #pk for the url parameter