from rest_framework import serializers 
from .models import Students, Scores

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'address', 'email']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = ['name', 'math', 'science', 'english']