from django import forms
from .models import Post

class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        #어떤 항목을 입력받을지
        fields = ['title', 'body']
