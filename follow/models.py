from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from post.models import Post

# Create your models here.

class Follow(models.Model):
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

# Streams post to all the users that are following the current user
class Stream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_following')
    date = models.DateTimeField()

    def load_post(sender, instance, *args, **kwargs):
        post = instance
        user = post.user
        # All the users whose FOLLOWING list includes the current user
        followers = Follow.objects.all().filter(following=user)

        for f in followers:
            stream = Stream(post=post, user=f.followers, date=post.created_at, following=user)
            stream.save()

post_save.connect(Stream.load_post, sender=Post)
