from django.db import models

# Create your models here.
class Post(models.Model):
    uploadfrom = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    