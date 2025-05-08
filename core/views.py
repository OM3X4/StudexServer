from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.db.models import Prefetch
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes




# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserData(request):
    user = User.objects.prefetch_related(
        Prefetch('sessions' , queryset=Session.objects.select_related('subject' , 'topic' , 'tag')),
        Prefetch('subjects' , queryset=Subject.objects.prefetch_related('topics')),
        'tags',
        Prefetch('goals' , queryset=Goal.objects.select_related('subject' , 'topic')),
    ).get(id=request.user.id)
    serial = UserSerializer(user)
    return Response(data=serial.data , status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def postSubject(request):
    user = request.user
    serial = SubjectSerializer(data=request.data)
    if serial.is_valid():
        serial.save(user=user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def postTopic(request):
    user = request.user
    serial = TopicSerializer(data=request.data)
    if serial.is_valid():
        serial.save(user=user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def postTag(request):
    user = request.user
    serial = TagSerializer(data=request.data)
    if serial.is_valid():
        serial.save(user=user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logSession(request):
    user = request.user
    serial = SessionSerializer(data=request.data)
    if serial.is_valid():
        serial.save(user=user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def postGoal(request):
    user = request.user
    serial = GoalSerializer(data=request.data)
    if serial.is_valid():
        serial.save(user=user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        refresh = RefreshToken.for_user(serializer.instance)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': serializer.instance.username
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

