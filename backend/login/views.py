from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "login/register.html", context)


def homepage(request):
    return render(request, "login/home.html", {})


def loginpage(request):
    next_url = request.GET.get('next', '')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            if next_url:
                return redirect(next_url)
            return render(request, "login/home2.html", {})
        
        messages.error(request, "Invalid username or password")
        return render(request, "login/login_new.html", {"error": "Invalid username or password", "next": next_url})

    return render(request, "login/login_new.html", {"next": next_url})


@login_required(login_url='/login')
def predict_arrhythmia(request):
    # Add your prediction logic here
    return render(request, "login/prediction.html", {})


@login_required(login_url='/login')
def postlogin(request):
    return render(request, "login/home2.html", {})
