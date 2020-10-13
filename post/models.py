import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

# Create a seperate directory for each user to upload his/her files
def get_user_directory(instance, file):
    return 'user-{0}/{1}'.format(instance.user.username, file)


class Post(models.Model):
    # Creating our own id for the post
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_user_directory, null=False, verbose_name='Picture')
    caption = models.TextField(max_length=1000, verbose_name='Caption')
    location = models.CharField(max_length=100, null=True, blank=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Posts'
