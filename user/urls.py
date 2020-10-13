from django.urls import path
from django.contrib.auth import views as auth_views
from user import views as user_views

app_name = 'user'
urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout, name='logout'),
    path('change-password/', user_views.password_change, name='change-password'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='reset-password.html'), name='reset-password'),
]
