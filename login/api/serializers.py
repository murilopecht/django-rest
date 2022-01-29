from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import models

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.User