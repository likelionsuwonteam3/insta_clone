from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    uploadfrom = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like = models.IntegerField(default = 0)
    
    
    # liked posts of the post
    likedpost = models.ManyToManyField(User,related_name = 'member')
    
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    pup_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.comment


class PostLike(models.Model):
    postliker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likedpost = models.ForeignKey(Post, on_delete = models.CASCADE, null=True)

#  m:n 관계를 설정한다!
# 좋아요 누른 유저
# 좋아요 받은 글

# 1번 유저는 n개의 글을 좋아요 가능
# n번 글은 m명의 유저로부터 하트 받음

