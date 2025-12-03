from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  

# Post model for the blog application
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    # Add this method for redirect after creation
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

