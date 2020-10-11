from django.urls import path
from follow import views

app_name = 'follow'
urlpatterns = [
    path('', views.follow, name='follow'),
]
