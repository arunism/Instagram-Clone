from django.contrib import admin
from reaction.models import Like

# Register your models here.

class LikeAdmin(admin.ModelAdmin):
    search_fields = ['user', 'post']
    list_display = ['user', 'post']
    list_filter = ['user', 'post']
    readonly_fields = ['user', 'post']
    class Meta:
        model = Like

admin.site.register(Like, LikeAdmin)
