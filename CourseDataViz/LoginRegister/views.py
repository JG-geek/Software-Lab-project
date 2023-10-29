from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,Group

# Create your views here.
def index(request):
    # user = User.objects.get()
    g = Group.objects.get(name="Student")
    user = User.objects.create_user(
        "john", "lennon@thebeatles.com", "johnpassword")
    user.groups.add(g)
    user.save()
    
    return HttpResponse(user.groups.get())
