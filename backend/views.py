from rest_framework import serializers,status
# from django.views.decorators.csrf import csrf_exempt
from .models import UserList
from .serializer import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
# Create your views here.
class register(APIView):

    def get(self,request):
        print("get")
        users=UserList.queryset;
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    # @csrf_exempt
    def post(self, request):
        serializer =UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

