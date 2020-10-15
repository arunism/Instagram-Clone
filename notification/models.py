from django.db import models
from django.contrib.auth.models import User

# Create your models here.

NOTIFICATION_CHOICES = (
    ('Like', 'Like'),
    ('Comment', 'Comment'),
    ('Follow', 'Follow')
)

class Notification(models.Model):
    # Here we are not importing Post model but assigning in below way to avoid circular import
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, null=True, blank=True, related_name='post_notification')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_from')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_to')
    comment_body = models.CharField(max_length=200)
    type = models.CharField(choices=NOTIFICATION_CHOICES, max_length=10)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
