from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from djangocrud.api.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):


    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
