# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .permissions import DataOwner
from rest_framework import status

from .serializers import UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model # If used custom user model

User = get_user_model()

# @cache_page(60)
class UserView(CreateAPIView, ListAPIView):

    model = User
    serializer_class = UserSerializer
    filterset_fields = ['name', 'email', 'phoneNumber']

  
    def get_queryset(self):
       
        """
        This view should return a list of all the user active.
        """
        user = self.request.user
        return User.objects

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(UserView, self).dispatch(*args, **kwargs)
    
class UserUpdate(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    permission_classes = [DataOwner]
    serializer_class = UserSerializer
    queryset = User.objects.all()



