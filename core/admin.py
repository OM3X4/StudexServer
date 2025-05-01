from django.contrib import admin
from .models import Subject , Session , Tag , Goal , Topic

# Register your models here.
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Goal)
admin.site.register(Tag)
admin.site.register(Session)
