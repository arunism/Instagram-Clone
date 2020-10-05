from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'title': 'Feeds'}
    return render(request, 'feed.html', context)
