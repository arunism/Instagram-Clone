from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import resolve
from django.contrib.auth.models import User
from post.models import Post
from follow.models import Follow
from user_profile.models import Profile

# Create your views here.

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    post_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(followers=user).count()
    followers_count = Follow.objects.filter(following=user).count()

    context = {
        'title': 'Profile',
        'profile':profile,
        'posts':posts,
        'post_count':post_count,
        'following_count':following_count,
        'followers_count':followers_count
    }
    return render(request, 'profile.html', context)
