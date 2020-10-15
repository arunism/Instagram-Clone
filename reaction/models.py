from django.db import models
from django.contrib.auth.models import User
from post.models import Post

# Create your models here.

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    body = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True, auto_now=False)
