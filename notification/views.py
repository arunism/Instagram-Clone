from django.shortcuts import render
from notification.models import Notification

# Create your views here.

def notification(request):
    user = request.user
    notifications = Notification.objects.filter(receiver=user).order_by('-created_at')

    context = {'title': 'Notifications', 'notifications':notifications}
    return render(request, 'notification.html', context)
