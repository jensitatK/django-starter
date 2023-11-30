import uuid
from django.db import models
from .models import User
from rest_framework import serializers
from rest_framework.fields import UUIDField


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'age']
    