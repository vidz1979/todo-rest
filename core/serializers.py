# coding: utf-8
from rest_framework import serializers
from .models import Task, Tag
from django.contrib.auth.models import User

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # owner e created_at são colocados como read_only ao utilizar serializes.Field
    owner = serializers.Field(source='owner.username')
    created_at = serializers.Field(source='created_at')
    uri = serializers.HyperlinkedIdentityField(view_name='task-detail', format='html')

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done', 'created_at', 'owner', 'uri')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    uri = serializers.HyperlinkedIdentityField(view_name='user-detail', format='html')

    class Meta:
        model = User
        fields = ('id', 'username', 'uri')
