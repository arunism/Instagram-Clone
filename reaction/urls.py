from django.urls import path
from reaction import views

app_name = 'reaction'
urlpatterns = [
    path('<uuid:id>/likes/', views.likes, name='likes'),
]
