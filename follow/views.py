from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from follow.models import Follow, Stream
from post.models import Post

# Create your views here.

@login_required
def follow(request, username, option):
    user = request.user
    following = get_object_or_404(User, username=username)

    try:
        f, created = Follow.objects.get_or_create(followers=user, following=following)
        if int(option) == 0:
            f.delete()
            Stream.objects.filter(following=following, user=user).all().delete()
        else:
            posts = Post.objects.all().filter(user=following)
            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=user, following=following, date=post.created_at)
                    stream.save()
        return HttpResponseRedirect(reverse('profile:profile', args=[username]))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile:profile', args=[username]))
