from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):    
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #Automatically checked by django.
            form.save() #That hashes the password to make it secure, and saves the user.
            username = form.cleaned_data.get('username') #Already validated
            messages.success(request, f'Thank for creating an account, {username}! You are now able to log in.') #Other options are: info, success, warning, error
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#The login_required decorator adds functionality to the profile view.
#It will automatically redirect to the page that the user tried to access if the verification is successful.
#http://localhost:8000/login/?next=/profile/
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) #instance=request.user gets the logged-in user.
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile) # And that gets the logged-in user's profile.
        if u_form.is_valid() and p_form.is_valid():
            username = u_form.cleaned_data.get('username') #Already validated
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated, {username}.') #Other options are: info, success, warning, error
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user) #instance=request.user gets the logged-in user.
        p_form = ProfileUpdateForm(instance=request.user.profile) # And that gets the logged-in user's

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

