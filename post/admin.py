from django.contrib import admin
from post.models import Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['user', 'created_at', 'updated_at']
    list_display = ['user', 'id']
    # list_editable = ['new_price', 'available']
    list_filter = ['user', 'created_at', 'likes']
    readonly_fields = ['id', 'user', 'tags', 'photo', 'caption', 'location', 'likes', 'created_at', 'updated_at']
    class Meta:
        model = Post

class TagAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'slug']
    readonly_fields = ['title', 'slug']
    class Meta:
        model = Tag

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
