from django.urls import path
from .views import getUserData , postSubject , postTag , postTopic , logSession

urlpatterns = [
    path('user/' , getUserData),
    path('subject/' , postSubject),
    path('tag/' , postTag),
    path('topic/' , postTopic),
    path('log/' , logSession),
]