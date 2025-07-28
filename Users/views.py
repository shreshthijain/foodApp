from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # messages.success(request, f"Welcome {username} to our app")
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "Users/register.html", {'form':form})