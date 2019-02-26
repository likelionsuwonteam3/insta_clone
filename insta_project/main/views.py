from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Post
from .forms import BlogPost
from django.utils import timezone

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        post = Post.objects
        return render(request, 'home.html', {'post': post})
    else:
        return render(request, 'no.html')    

def new(request):

    form = BlogPost()
    return render(request, 'new.html', {'form' : form})


def create(request):
    if request.method=="POST":
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            #모델 객체형태 post이지만 저장은 하지마라!
            post = form.save(commit=False)
            # post.image=request.POST['uploadfrom']
            post.uploadfrom = request.FILES['uploadfrom']
            post.author = request.user
            post.pub_date = timezone.now()
            post.body=request.POST['body']
            
            post.save()
            return redirect('home')
        else:
            return render(request,'new.html', {'form' : form} )
    else: # get 방식
        form = BlogPost()
        return render(request, 'new.html', {'form' : form})

