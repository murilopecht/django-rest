from rest_framework import viewsets, permissions
from login.api import serializers
from django.contrib.auth import models

class UserViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permissions_classes = (permissions.IsAuthenticated)
    
    def get_queryset(self):
        return self.queryset
    
    
    
    
    