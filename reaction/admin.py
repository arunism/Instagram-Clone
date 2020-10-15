from django.contrib import admin
from reaction.models import Like, Comment

# Register your models here.

class LikeAdmin(admin.ModelAdmin):
    search_fields = ['user', 'post']
    list_display = ['user', 'post']
    list_filter = ['user', 'post']
    readonly_fields = ['user', 'post']
    class Meta:
        model = Like

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['user', 'post']
    list_display = ['user', 'post']
    list_filter = ['user', 'post']
    readonly_fields = ['user', 'post', 'body', 'commented_at']
    class Meta:
        model = Comment

admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
