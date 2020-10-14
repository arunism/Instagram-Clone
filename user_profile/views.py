from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import resolve
from django.contrib.auth.models import User
from post.models import Post
from follow.models import Follow
from user_profile.models import Profile
from user_profile.forms import EditProfileForm

# Create your views here.

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    post_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(followers=user).count()
    followers_count = Follow.objects.filter(following=user).count()
    follow_status = Follow.objects.filter(followers=request.user, following=user).exists()

    context = {
        'title': 'Profile',
        'profile':profile,
        'posts':posts,
        'post_count':post_count,
        'following_count':following_count,
        'followers_count':followers_count,
        'follow_status': follow_status
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(user__id=user.id)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.nickname = form.cleaned_data.get('nickname')
            profile.phone = form.cleaned_data.get('phone')
            profile.location = form.cleaned_data.get('location')
            profile.website = form.cleaned_data.get('website')
            profile.bio = form.cleaned_data.get('bio')
            profile.gender = form.cleaned_data.get('gender')
            profile.save()
            return HttpResponseRedirect(reverse('profile:profile', args=[user.username]))
    else:
        form = EditProfileForm()
    context = {'title':'Edit Profile', 'form':form}
    return render(request, 'edit-profile.html', context)
