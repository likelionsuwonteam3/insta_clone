from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Post, Comment
from .forms import BlogPost
from django.utils import timezone

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        post = Post.objects
        comment = Comment.objects
        return render(request, 'home.html', {'post': post, 'comment': comment})
    else:
        return render(request, 'no.html')    

def new(request):

    form = BlogPost()
    return render(request, 'new.html', {'form' : form})

def like(request, post_id):
    likedPost = get_object_or_404(Post, pk=post_id)
    likedPost.like += 1
    print("==================")
    print("request.user.member : ")
    print(request.user.member)
    print("==================")
    likedPost = request.user
    print("==================")
    print("likedPost : ")
    print(likedPost)
    print("==================")
    likedPost.save()
    return redirect('home')

def comment(request, post_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment = Comment()
            comment.comment = request.POST['inputComment']
            comment.pup_date = timezone.datetime.now()
            comment.author = request.user
            comment.post = Post.objects.get(id=post_id)
            comment.save()
            return redirect('home')
        else:
            return redirect('login')
    else:
        return HttpResponseNotFound("없는 페이지 입니다.")
    return redirect('home')

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

