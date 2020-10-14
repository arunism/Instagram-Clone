from django.urls import path
from user_profile import views

app_name = 'profile'
urlpatterns = [
    path('<username>/', views.profile, name='profile'),
    path('edit/info/', views.edit_profile, name='edit-profile'),
]
