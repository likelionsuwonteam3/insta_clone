from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    