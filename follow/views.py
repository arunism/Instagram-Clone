from django.shortcuts import render

# Create your views here.

def follow(request):
    context = {'title': 'Follow'}
    return render(request, 'explore.html', context)
