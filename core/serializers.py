from rest_framework import serializers
from .models import Session , Subject , Topic , Tag , Goal
from django.contrib.auth.models import User



class SessionSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.subject' , read_only=True)
    topic_name = serializers.CharField(source='topic.topic' , read_only=True)
    tag_name = serializers.CharField(source='tag.tag' , read_only=True)


    class Meta:
        model = Session
        fields = ['id' ,  'subject' , 'subject_name' ,'topic' , 'topic_name' , 'tag' , 'tag_name' , 'focus' , 'start' , 'end']




class TopicSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.subject', read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'topic', 'subject_name']

class SubjectSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True , read_only=True)


    class Meta:
        model = Subject
        fields = ['id' , 'subject' , 'topics']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']

class GoalSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.subject" , read_only=True)
    topic_name = serializers.CharField(source="topic.topic" , read_only=True)
    tag_name = serializers.CharField(source="tag.tag" , read_only=True)


    class Meta:
        model = Goal
        fields = ['id', 'end' , 'minutes' , 'subject' , 'topic' , 'tag' , 'tag_name' , 'subject_name' , 'topic_name' ]



class UserSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    # topics = TopicSerializer(many=True, read_only=True)
    goals = GoalSerializer(many=True , read_only=True)
    tags = TagSerializer(many=True , read_only=True)
    sessions = SessionSerializer(many=True , read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'subjects' , 'sessions' , 'goals' ,'tags']