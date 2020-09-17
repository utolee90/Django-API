from rest_framework import serializers 
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user= User.objects.create(
            username=validated_data['username'],
            phone_number = validated_data['phone_number'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password']) #password 암호화 저장
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ['username', 'password', 'phone_number', 'email']
