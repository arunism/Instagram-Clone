from django.contrib import admin
from notification.models import Notification

# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['receiver', 'sender', 'created_at']
    list_display = ['sender', 'receiver']
    # list_editable = ['new_price', 'available']
    list_filter = ['sender', 'receiver', 'created_at']
    readonly_fields = ['post', 'sender', 'receiver', 'type', 'seen', 'comment_body', 'created_at']
    class Meta:
        model = Notification

admin.site.register(Notification, NotificationAdmin)
