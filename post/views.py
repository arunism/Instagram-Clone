from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q
from post.models import Post
from follow.models import Stream
from reaction.models import Like, Comment
from reaction.forms import CommentForm
from post.forms import CreatePostForm

# Create your views here.

@login_required
def feeds(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    post_list = []

    for post in posts:
        post_list.append(post.post_id)

    all_posts = Post.objects.filter(id__in=post_list).all().order_by('-created_at')

    context = {'title': 'Feeds', 'all_posts':all_posts}
    return render(request, 'feed.html', context)

@login_required
def create_post(request):
    user = request.user.id

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.cleaned_data.get('photo')
            caption = form.cleaned_data.get('caption')
            location = form.cleaned_data.get('location')

            p, created_at = Post.objects.get_or_create(photo=photo, caption=caption, user_id=user)
            p.save()
            return redirect('post:home')
    else:
        form = CreatePostForm()

    context = {'title':'Create New Post', 'form':form, 'user':request.user}
    return render(request, 'create-post.html', context)

@login_required
def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post).order_by('commented_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('post:post_details', args=[id]))
    else:
        form = CommentForm()

    context = {'title':'Post Details', 'post':post, 'form':form, 'comments':comments}
    return render(request, 'post-detail.html', context)

@login_required
def search(request):
    try:
        query = request.GET['query']
    except:
        query = None
    if query:
        users = User.objects.all()
        users = users.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
        # __iexact for exact match
    else:
        users = User.objects.all()
    context = {'title':'Search Results', 'users':users}
    return render(request, 'search.html', context)
