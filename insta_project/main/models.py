from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    uploadfrom = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like = models.IntegerField(default = 0)
    
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    pup_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.comment
    