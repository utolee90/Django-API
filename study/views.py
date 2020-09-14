from django.shortcuts import render
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views
from .models import Students
from .serializer import StudentSerializer


# Create your views here.
@api_view(['GET'])
def StudentView(request):
    qs = Students.objects.all()
    serializer = StudentSerializer(qs, many=True)
    return Response(serializer.data)
