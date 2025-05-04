from rest_framework import serializers
from .models import Session , Subject , Topic , Tag , Goal
from django.contrib.auth.models import User
from datetime import date
from .models import Session
from django.db.models import Sum


class SessionSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.subject' , read_only=True)
    topic_name = serializers.CharField(source='topic.topic' , read_only=True)
    tag_name = serializers.CharField(source='tag.tag' , read_only=True)


    class Meta:
        model = Session
        fields = ['id' ,  'subject' , 'subject_name' ,'topic' , 'topic_name' , 'tag' , 'tag_name' , 'focus' , 'duration']

class TopicSerializer(serializers.ModelSerializer):
    # subject_name = serializers.CharField(source='subject.subject', read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'topic']

class SubjectSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True , read_only=True)


    class Meta:
        model = Subject
        fields = ['id' , 'subject' , 'topics' , 'color']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']

class GoalSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.subject" , read_only=True)
    topic_name = serializers.CharField(source="topic.topic" , read_only=True)


    class Meta:
        model = Goal
        fields = ['id', 'end' , 'minutes' , 'subject' , 'topic' , 'subject_name' , 'topic_name' ]

class HeatMapEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['creation' , 'duration']

class UserSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    goals = GoalSerializer(many=True , read_only=True)
    tags = TagSerializer(many=True , read_only=True)
    sessions = SessionSerializer(many=True , read_only=True)

    studied_today = serializers.SerializerMethodField()
    studied_this_week = serializers.SerializerMethodField()
    studied_all_time = serializers.SerializerMethodField()

    heatmap = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'subjects' , 'sessions' , 'goals' ,'tags' , 'studied_today' , 'studied_this_week' , 'studied_all_time' , 'heatmap']

    def get_studied_today(self, obj):
        return Session.objects.filter(user=obj, creation__date=date.today()).aggregate(total_minutes=Sum('duration'))['total_minutes'] or 0

    def get_studied_this_week(self, obj):
        return Session.objects.filter(user=obj, creation__week=date.today().isocalendar()[1]).aggregate(total_minutes=Sum('duration'))['total_minutes'] or 0

    def get_studied_all_time(self, obj):
        return Session.objects.filter(user=obj).aggregate(total_minutes=Sum('duration'))['total_minutes'] or 0

    def get_heatmap(self , obj):
        return HeatMapEntitySerializer(Session.objects.filter(user=obj).order_by('creation') , many=True).data