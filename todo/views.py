from django.shortcuts import render, get_object_or_404
from django.urls import path, include
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import TodoGroup, Todo, FavouriteGroup, Favourite
from .serializers import TodoGroupSerializer, TodoSerializer, FavouriteGroupSerializer, FavouriteSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TodoAllSelectView(request):
    if request.method == 'GET':
        all = TodoSerializer(Todo.objects.all(), many=True)
        pending = TodoSerializer(Todo.objects.filter(status="Pending"), many=True)
        inprogress = TodoSerializer(Todo.objects.filter(status="Inprogress"), many=True)
        end = TodoSerializer(Todo.objects.filter(status="End"), many=True)
        return Response({
            "all": all.data,
            "inprogress": inprogress.data,
            "pending": pending.data,
            "end": end.data
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def FavouriteAllSelectView(request):
    if request.method == 'GET':
        favourite = FavouriteSerializer(Favourite.objects.all(), many=True)
        return Response(favourite.data)

class TodoGroupView(viewsets.ModelViewSet):
    queryset= TodoGroup.objects.all()
    serializer_class = TodoGroupSerializer

class TodoView(viewsets.ModelViewSet):
    queryset= Todo.objects.all()
    serializer_class = TodoSerializer

class FavouriteGroupView(viewsets.ModelViewSet):
    queryset= FavouriteGroup.objects.all()
    serializer_class = FavouriteGroupSerializer

class FavouriteView(viewsets.ModelViewSet):
    queryset= Favourite.objects.all()
    serializer_class = FavouriteSerializer


