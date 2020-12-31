from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email')
