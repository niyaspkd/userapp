from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import get_user_model # If used custom user model
from .serializers import UserSerializer
from .views import UserView, UserUpdate
from rest_framework.authtoken.views import obtain_auth_token  


urlpatterns = [
    path('list', UserView.as_view()),
    path('detail/<int:pk>', UserUpdate.as_view()),
    path('login/', obtain_auth_token, name='api_token_auth'),
    

  
]
