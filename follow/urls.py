from django.urls import path
from follow import views

app_name = 'follow'
urlpatterns = [
    path('<username>/<option>', views.follow, name='follow'),
]
