from rest_framework import serializers 
from .models import Students, Scores
from django.contrib.auth import get_user_model
from rest_framework.validators  import UniqueValidator, ValidationError
import re

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
    #reg_user = UserSerializer(read_only=True) #override
    reg_username = serializers.ReadOnlyField(source='reg_user.username') #등록하면 무조건 필드에 입력해야 한다
    reg_email = serializers.ReadOnlyField(source='reg_user.email') 
    reg_phone_number = serializers.ReadOnlyField(source='reg_user.phone_number') 
    name = serializers.CharField(max_length=10,
    validators= [UniqueValidator(queryset=Students.objects.all()) ])
    email = serializers.CharField(max_length=30)
    
    def validate_email(self, value):
        pat = r'[A-Za-z0-9\-_]+@[a-z0-9]+(\.[a-z])+'
        
        if bool(re.match(pat, value)) == False:
            raise ValidationError('이메일 형식이 아닙니다.')
        return value
    
    def validate_phone_number(self, value):
        pat = r'[0-9]{2,3}(\-?|\s)[0-9]{3,4}(\-?|\s)[0-9]{4}'

        if bool(re.match(pat, value)) == False:
            raise ValidationError('전화번호 형식이 아닙니다.')
        return value

    #test = serializers.SerializerMethodField()

    def get_test(self, obj):
        return obj.address+" ("+obj.name+")"

    class Meta:
        model = Students
        fields = ['name', 'address', 'email',  'memo', 
        'reg_user', 'reg_username', 'reg_email', 'reg_phone_number'
         #'test',
         ]
        

class ScoreSerializer(serializers.ModelSerializer):
    #reg_user = UserSerializer(read_only=True) #override
    reg_username = serializers.ReadOnlyField(source='reg_user.username')
    reg_email = serializers.ReadOnlyField(source='reg_user.email')
    reg_phone_number = serializers.ReadOnlyField(source='reg_user.phone_number')
    name = serializers.CharField(max_length=10,
    validators= [UniqueValidator(queryset=Students.objects.all()) ])
    
    def validate_math(self,value):
        if str(value).isnumeric() == False or int(value)>100:
            raise ValidationError('점수 형식이 아닙니다.')
        return value
    
    def validate_english(self,value):
        if str(value).isnumeric() == False or int(value)>100:
            raise ValidationError('점수 형식이 아닙니다.')
        return value

    def validate_science(self,value):
        if str(value).isnumeric() == False or int(value)>100:
            raise ValidationError('점수 형식이 아닙니다.')
        return value



    class Meta:
        model = Scores
        fields = ['name', 'math', 'english', 'science', 'reg_user', 'reg_username', 'reg_email', 'reg_phone_number']