from django.shortcuts import render, get_object_or_404
from django.urls import path, include
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from . import views
from .models import Students, Scores
from .serializer import StudentSerializer, ScoreSerializer, StudentBasicSerializer, ScoreBasicSerializer

# Viewsets

class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name=name)
        return qs
    @action(detail=False, methods=['GET'])
    def incheon(self, requset):
        qs = self.get_queryset().filter(address__contains='인천') # like '%인천%'
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['PUT'])
    def init(self, requset, pk): #url pk/init
        instance = self.get_object()
        instance.address = ""
        instance.email = ""
        instance.save(update_fields=['address','email'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    
class ScoreView(viewsets.ModelViewSet):
    queryset = Scores.objects.all()
    serializer_class = ScoreSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        math = self.request.query_params.get('math')
        english = self.request.query_params.get('english')
        science = self.request.query_params.get('science')
        order = self.request.query_params.get('order')
        if name:
            qs = qs.filter(name=name)
        if math:
            qs = qs.filter(math__gte=math)
        if english:
            qs = qs.filter(english__gte=english)
        if science:
            qs = qs.filter(science__gte=science)
        if order:
            qs = qs.order_by(order)
        return qs
    
    @action(detail=False, methods=['GET'])
    def top(self, requset):
        from django.db.models import F
        #qs = self.get_queryset().filter()
        qs = self.get_queryset().filter(math__gte=80, english__gte=80, science__gte=80) # like '%인천%'
        qs1 = self.get_queryset().annotate(ssum=F('math')+F('science')+F('english')).filter(ssum__gte=270)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def StudentBasicView(request):
    if request.method == 'GET':
        student = Students.objects.all()
        print('1')
        serializer = StudentBasicSerializer(student, many=True)
        print('2')
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentBasicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT'])
def StudentDetailBasicView(request, pk):
    student = Students.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = StudentBasicSerializer(student)
        return Response(serializer.data)
    if request.method == 'PUT':
        #student 원래데이터
        #request.data 사람이 보내준 데이터
        #(원래데이터 <- 사람이 보내준 데이터) -> SAVE 
        serializer = StudentBasicSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def ScoreBasicView(request):
    if request.method == 'GET':
        scores = Scores.objects.all()
        serializer = ScoreBasicSerializer(scores, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ScoreBasicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
def ScoreDetailBasicView(request, pk):
    score = Scores.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ScoreBasicSerializer(score)
        return Response(serializer.data)
    if request.method == 'PUT':
        #student 원래데이터
        #request.data 사람이 보내준 데이터
        #(원래데이터 <- 사람이 보내준 데이터) -> SAVE 
        serializer = StudentBasicSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# class StudentView(APIView):
    
#     def get(self, request):
#         qs = Students.objects.all()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             student =  Students.objects.get(pk=pk)
#         except:
#             raise Http404()
#         return student
    
#     def get(self, request, pk):
#         qs = self.get_object(pk)
#         serializer = StudentSerializer(qs)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         qs = self.get_object(pk)
#         serializer = StudentSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def delete(self, request, pk):
#         qs = self.get_object(pk)
#         qs.delete()
#         return Response(status=204)

# class ScoreView(APIView):
    
#     def get(self, request):
#         qs = Scores.objects.all()
#         serializer = ScoreSerializer(qs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ScoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ScoreDetailView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Scores, pk=pk)
    
#     def get(self, request, pk):
#         qs = self.get_object(pk)
#         serializer = ScoreSerializer(qs)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         qs = self.get_object(pk)
#         serializer = ScoreSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def delete(self, request, pk):
#         qs = self.get_object(pk)
#         qs.delete()
#         return Response(status=204)


# # Create your views here.
# @api_view(['GET', 'POST'])
# def StudentView(request):
#     if request.method == 'GET':
#         qs = Students.objects.all()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def StudentDetailView(request, id):
#     qs = get_object_or_404(Students, pk=id)
#     if request.method == 'GET':
#         serializer = StudentSerializer(qs)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.data, status=400)
#     elif request.method == "DELETE":
#         qs.delete()
#         return Response(status=204)

# @api_view(['GET', 'POST'])
# def ScoreView(request):
#     if request.method == 'GET':
#         qs = Scores.objects.all()
#         serializer = ScoreSerializer(qs, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ScoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def ScoreDetailView(request, id):
#     qs = get_object_or_404(Scores, id=id)
#     print(qs)
#     if request.method == 'GET':
#         serializer = ScoreSerializer(qs)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ScoreSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.data, status=400)
#     elif request.method == "DELETE":
#         qs.delete()
#         return Response(status=204)

