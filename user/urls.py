from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('change-password/', views.password_change, name='password_change'),
]
