from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# from django.http import HttpResponse <- Not required anymore.

# Create your views here.
def home(request):    
    contextPosts = {
        'posts': Post.objects.all() #Just as you would run it from the shell.
    }
    return render(request, 'blog/home.html', contextPosts)

class PostListView(ListView): #Inherits from the ListView
    model = Post
    template_name = "blog/home.html"
    # <app>/<model>_<viewtype>.html <- Default (like with the detail view of the individual post.)
    context_object_name = 'posts' #<- Just like in the home function above.
    ordering = ['-date_posted'] # <- Newest to oldest. ['date_posted'] <- Oldest to newest.
    paginate_by = 5

class UserPostListView(ListView): #Inherits from the ListView
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts' #<- Just like in the home function above.
    paginate_by = 5

    def get_queryset(self):
        #If the user with that username exists, it will be stored in the 'user' variable.
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView): #Inherits from the ListView
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        #We set the author of the (Post) instance = current logged-in user.
        form.instance.author = self.request.user
        #We run the form_valid() method on our parent class, but we assign the author to it before it runs.
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        #We set the author of the (Post) instance = current logged-in user.
        form.instance.author = self.request.user
        #We run the form_valid() method on our parent class, but we assign the author to it before it runs.
        return super().form_valid(form)
    
    #Ran by UserPassesTestMixin to see if the user passes certain test conditions.
    def test_func(self):
        post = self.get_object()
        #We check if the user trying to update the post is equal to the author of that post. 
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    #Ran by UserPassesTestMixin to see if the user passes certain test conditions.
    def test_func(self):
        post = self.get_object()
        #We check if the user trying to update the post is equal to the author of that post. 
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
