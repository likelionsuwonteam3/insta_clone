from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Post
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        post = Post.objects
        return render(request, 'home.html', {'post': post})
    else:
        return render(request, 'no.html')    