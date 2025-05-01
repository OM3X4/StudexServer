from django.urls import path
from .views import getUserData

urlpatterns = [
    path('user/' , getUserData)
]