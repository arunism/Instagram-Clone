from django.shortcuts import render
from post.models import Post
from follow.models import Stream

# Create your views here.

def feeds(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    post_list = []

    for post in posts:
        post_list.append(post.post_id)

    all_posts = Post.objects.filter(id__in=post_list).all().order_by('-created_at')
    
    context = {'title': 'Feeds', 'all_posts':all_posts}
    return render(request, 'feed.html', context)
