from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.db.models import Prefetch


# Create your views here.
@api_view(["GET"])
def getUserData(request):
    user = User.objects.prefetch_related(
        Prefetch('sessions' , queryset=Session.objects.select_related('subject' , 'topic' , 'tag')),
        Prefetch('subjects' , queryset=Subject.objects.prefetch_related('topics')),
        'tags',
        Prefetch('goals' , queryset=Goal.objects.select_related('subject' , 'topic')),
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
    return Response(status=status.HTTP_400_BAD_REQUEST)

