from rest_framework import serializers 
from .models import TodoGroup, Todo, FavouriteGroup, Favourite 
from django.contrib.auth import get_user_model
from rest_framework.validators  import UniqueValidator, ValidationError
import re


class TodoGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoGroup
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Todo
        fields = ['seq', 'name', 'status', 'end_date', 'image', 'group', 'group_name']

class FavouriteGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteGroup
        fields = '__all__'

class FavouriteSerializer(serializers.ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Favourite
        fields = ['seq', 'name', 'url', 'memo', 'reg_date', 'group', 'group_name']