from django.shortcuts import render, get_object_or_404
from django.urls import path, include
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views
from .models import Students, Scores
from .serializer import StudentSerializer, ScoreSerializer

#
class StudentView(APIView):
    
    def get(self, request):
        qs = Students.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get_object(self, pk):
        try:
            student =  Students.objects.get(pk=pk)
        except:
            raise Http404()
        return student
    
    def get(self, request, pk):
        qs = self.get_object(pk)
        serializer = StudentSerializer(qs)
        return Response(serializer.data)
    
    def put(self, request, pk):
        qs = self.get_object(pk)
        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        qs = self.get_object(pk)
        qs.delete()
        return Response(status=204)

class ScoreView(APIView):
    
    def get(self, request):
        qs = Scores.objects.all()
        serializer = ScoreSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScoreDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Scores, pk=pk)
    
    def get(self, request, pk):
        qs = self.get_object(pk)
        serializer = ScoreSerializer(qs)
        return Response(serializer.data)
    
    def put(self, request, pk):
        qs = self.get_object(pk)
        serializer = ScoreSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        qs = self.get_object(pk)
        qs.delete()
        return Response(status=204)


"""
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

"""