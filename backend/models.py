from django.db import models
from django.contrib.auth.models import User
from .serializer import UserSerializer 
# Create your models here.
class UserList():
    queryset = User.objects.all()

