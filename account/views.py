from django.shortcuts import render
from .models import User
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def Signup(request):
    if request.method == 'GET':
        users = SignupSerializer(User.objects.all(), many=True)
        return Response(users.data)

    elif request.method == 'POST':
        signup = SignupSerializer(data=request.data)
        if signup.is_valid():
            signup.save()
            return Response(signup.data, status=201)
        return Response(signup.errors, status=400)            

