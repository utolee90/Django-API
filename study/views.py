from django.shortcuts import render, get_object_or_404
from django.urls import path, include
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views
from .models import Students, Scores
from .serializer import StudentSerializer, ScoreSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def StudentView(request):
    if request.method == 'GET':
        qs = Students.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailView(request, id):
    qs = get_object_or_404(Students, pk=id)
    if request.method == 'GET':
        serializer = StudentSerializer(qs)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=400)
    elif request.method == "DELETE":
        qs.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def ScoreView(request):
    if request.method == 'GET':
        qs = Scores.objects.all()
        serializer = ScoreSerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def ScoreDetailView(request, id):
    qs = get_object_or_404(Scores, id=id)
    print(qs)
    if request.method == 'GET':
        serializer = ScoreSerializer(qs)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ScoreSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=400)
    elif request.method == "DELETE":
        qs.delete()
        return Response(status=204)

