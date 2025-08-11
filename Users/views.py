from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from Users.models import UserProfile
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # messages.success(request, f"Welcome {username} to our app")
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Error in registration. Please try again.")
    else:
        form = RegisterForm()
    return render(request, "Users/register.html", {'form':form})

@login_required
def profile(request):
    if not hasattr(request.user, 'userprofile'):
        UserProfile.objects.create(user=request.user)
    profile = request.user.userprofile
    return render(request, 'Users/profile.html', {'profile': profile})