from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username')
    
    def create(self, validated_data):
        print(validated_data)
        username=validated_data.get('username',None)
        email=validated_data.get('email',None)
        password=validated_data.get('password',None)
        print(password)
        return User.objects.create_user(username=username,email=email,password=password)
    
