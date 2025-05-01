from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.models import User


# Create your views here.
@api_view(["GET"])
def getUserData(request):
    user = User.objects.first()
    serial = UserSerializer(user)
    return Response(data=serial.data , status=status.HTTP_200_OK)
