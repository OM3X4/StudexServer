from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='subjects')
    subject = models.CharField(max_length=200)
    color = models.CharField(max_length=16 , default="#1d5fc2" , blank=True)

    def __str__(self):
        return self.subject

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='topics')
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE , related_name='topics')
    topic = models.CharField(max_length=200)

    def __str__(self):
        return self.topic


class Tag(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='tags')
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.tag

class Session(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='sessions')
    subject = models.ForeignKey(Subject , on_delete=models.SET_NULL , null=True , blank=True)
    topic = models.ForeignKey(Topic , on_delete=models.SET_NULL , null=True , blank=True )
    tag = models.ForeignKey(Tag , on_delete=models.SET_NULL , null=True , blank=True)
    focus = models.SmallIntegerField()
    duration = models.IntegerField(default=60 , null=False) #minutes
    creation = models.DateTimeField(auto_now_add=True)


class Goal(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='goals')
    end = models.DateField()
    minutes = models.BigIntegerField()
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE , null=True , blank=True)
    topic = models.ForeignKey(Topic , on_delete=models.CASCADE , null=True , blank=True)
