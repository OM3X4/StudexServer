from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.models import User


# Create your views here.
@api_view(["GET"])
def getUserData(request):
    user = User.objects.select_related(
        'subjects',         # Use select_related for ForeignKey relationships
        'subjects__topic',  # This will load the topic data for each subject
        'goals',            # Select related goals for the user
        'tags',             # Select related tags for the user
        'sessions'          # Select related sessions for the user
    ).prefetch_related(
        'subjects__topics', # Still using prefetch for related many-to-many
        'goals',            # Pre-fetch goals, sessions, tags if needed
        'sessions'
    ).first()
    serial = UserSerializer(user)
    return Response(data=serial.data , status=status.HTTP_200_OK)


@api_view(["POST"])
def postSubject(request):
    user = User.objects.first()
    serial = SubjectSerializer(data=request.data)
    if serial.is_valid():
        serial.save(user=user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def postTopic(request):
    user = User.objects.first()
    serial = TopicSerializer(data=request.data)
    if serial.is_valid():
        serial.save(user=user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def postTag(request):
    user = User.objects.first()
    serial = TagSerializer(data=request.data)
    if serial.is_valid():
        serial.save(user=user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def logSession(request):
    user = User.objects.first()
    serial = SessionSerializer(data=request.data)
    if serial.is_valid():
        serial.save(user=user)
        return Response(status=status.HTTP_202_ACCEPTED)

