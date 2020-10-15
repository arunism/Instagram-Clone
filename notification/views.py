from django.shortcuts import render
from notification.models import Notification

# Create your views here.

def notification(request):
    user = request.user
    notifications = Notification.objects.filter(receiver=user).order_by('-created_at')
    Notification.objects.filter(receiver=user, seen=False).update(seen=True)

    context = {'title': 'Notifications', 'notifications':notifications}
    return render(request, 'notification.html', context)

def notification_counts(request):
    user = request.user
    count = 0
    if user.is_authenticated:
        count = Notification.objects.filter(receiver=user, seen=False).count()

    return {'notification_count':count}
