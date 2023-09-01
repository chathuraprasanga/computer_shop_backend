from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #adding for user loging authenticate
from django.contrib import messages #for sent frontend messages
from .forms import SignUpForm

# Create your views here.

# when frontend request home
def home(request):
    return render(request, 'home.html',{})

#login user function
def login_user(request):
    # check if to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # ?authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Successfully Logged In.!")
            return redirect('dashboard')
        else :
            messages.error(request,"There Was a Error In Login.!")
            return redirect('login')
    else:
        return render(request, 'login.html',{})

#logout user function
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Successfully Loged Out.!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate( username=username,password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Logged In.!")
            return redirect('home')
    else:
         form = SignUpForm()
         return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def dashboard(request):
    return render(request, 'dashboard.html', {})
