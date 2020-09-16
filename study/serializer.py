from rest_framework import serializers 
from .models import Students, Scores
from django.contrib.auth import get_user_model

class StudentBasicSerializer(serializers.Serializer): #커스텀 필요할 때 사용
    name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        Students.objects.create()
        return Students.objects.create(**validated_data)
        #return Students.objects.create(name=validated_data['name'], address=validated_data['address'])
    #student, data=request.data
    #inctance 원래데이터 (student)
    #validated_data 사람이 보내준 데이터 (data=request.data)
    #(원래데이터 <- 사람이 보내준 데이터) -> SAVE 
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.name)
        instance.email = validated_data.get('email', instance.name)
        instance.save()
        return instance

class ScoreBasicSerializer(serializers.Serializer): #커스텀 필요할 때 사용
    name = serializers.CharField()
    math = serializers.IntegerField()
    english = serializers.IntegerField()
    science = serializers.IntegerField()

    def create(self, validated_data):
        Scores.objects.create()
        return Scores.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.math = validated_data.math('math', instance.math)
        instance.english = validated_data.get('english', instance.english)
        instance.science = validated_data.get('science', instance.science)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    #reg_user = UserSerializer(read_only=True)
    #reg_username = serializers.ReadOnlyField(source='reg_user.username')
    #reg_email = serializers.ReadOnlyField(source='reg_user.email') 

    #test = serializers.SerializerMethodField()

    def get_test(self, obj):
        return obj.address+" ("+obj.name+")"

    class Meta:
        model = Students
        fields = ['name', 'address', 'email', 'memo', 'reg_user',
         #'test',
         ]

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = '__all__'