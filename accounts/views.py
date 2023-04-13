from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accounts.forms import Utilisateur


# Create your views here.
user=''
# inscription du candidat
def signunviews(request):
    if request.method =="POST":
        form = Utilisateur(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    else:
        form = Utilisateur()
    return render(request, 'signup.html', {'form':form})

# connexion du candidat
def Login_user(request):
    user=''
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('pro')
        
        else:
            return redirect('log_error')
        
    else:
        return render(request, 'login.html',{'user':user})
    
def index(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def log_error(request):
    return render(request, 'log_error.html')

