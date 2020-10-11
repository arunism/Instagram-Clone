from django.contrib import admin
from follow.models import Follow, Stream

# Register your models here.

class StreamAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    search_fields = ['user', 'following']
    list_display = ['user', 'post']
    # list_editable = ['new_price', 'available']
    list_filter = ['user', 'date']
    readonly_fields = ['user', 'post', 'following', 'date']
    class Meta:
        model = Stream

class FollowAdmin(admin.ModelAdmin):
    list_display = ['following', 'followers']
    search_fields = ['following', 'followers']
    list_filter = ['following', 'followers']
    readonly_fields = ['following', 'followers']
    class Meta:
        model = Follow

admin.site.register(Stream, StreamAdmin)
admin.site.register(Follow, FollowAdmin)
