from django.contrib import admin
from user_profile import models

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['user', 'first_name', 'last_name', 'location']
    list_display = ['user', 'first_name', 'last_name', 'location']
    # list_editable = ['new_price', 'available']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['user', 'first_name', 'last_name', 'nickname', 'phone', 'location', 'website', 'bio', 'picture', 'gender', 'created_at', 'updated_at']
    class Meta:
        model = models.Profile

admin.site.register(models.Profile, ProfileAdmin)
