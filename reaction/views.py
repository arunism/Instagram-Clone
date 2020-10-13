from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from reaction.models import Like
from post.models import Post

# Create your views here.

@login_required
def likes(request, id):
    user = request.user
    post = Post.objects.get(id=id)
    current_likes = post.likes
    liked = Like.objects.filter(user=user, post=post).count()

    if not liked:
        liked = Like.objects.create(user=user, post=post)
        current_likes += 1
    else:
        Like.objects.filter(user=user, post=post).delete()
        current_likes -= 1

    post.likes = current_likes
    post.save()

    return HttpResponseRedirect(reverse('post:post_details', args=[id]))
