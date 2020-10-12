from django.contrib import admin
from post.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['user', 'created_at', 'updated_at']
    list_display = ['user', 'id']
    # list_editable = ['new_price', 'available']
    list_filter = ['user', 'created_at', 'likes']
    readonly_fields = ['id', 'user', 'photo', 'caption', 'location', 'likes', 'created_at', 'updated_at']
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
