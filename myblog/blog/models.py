from datetime import timezone
from django.conf import settings
from registration.models import CustomUser

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts')

    def __str__(self):
        return f"post on {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    def total_likes(self):
        return self.likes.count()

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by someone on {self.post}"
