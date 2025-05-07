from django.urls import path
from .views import getUserData , postSubject , postTag , postTopic , logSession , postGoal , register_user

urlpatterns = [
    path('user/' , getUserData),
    path('subject/' , postSubject),
    path('tag/' , postTag),
    path('topic/' , postTopic),
    path('log/' , logSession),
    path('goal/' , postGoal),
    path('register/' , register_user),
]