from django.urls import path
from notification import views

app_name = 'notification'
urlpatterns = [
    path('', views.notification, name='notification'),
]
