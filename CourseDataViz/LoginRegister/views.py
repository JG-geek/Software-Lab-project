from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group,auth
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if (user is not None):
            auth.login(request,user)
            return redirect('/home')       
        else:
            return HttpResponse("Invalid login credentials")
    
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username,first_name=first_name, last_name=last_name,password=password,email=email)
        user.save()
        return redirect('/login')

def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/getLoginPage/')
def secret(request):
    return render(request, 'secret.html')