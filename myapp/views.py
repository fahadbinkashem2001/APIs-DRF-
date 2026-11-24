from django.shortcuts import get_object_or_404
from .models import Task,Author,Book,Student,University
from .serializers import TaskSerializer,AuthorSerializer,BookSerializer,StudentSerializer,UniversitySerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def task_list(request):
    if request.method == "GET":
        tasks = Task.objects.all() #queryset->fetch all the tasks from the database
        serializer = TaskSerializer(tasks, many=True) #serializer: converts the queryset into dict(python data)
        return Response(serializer.data, status=status.HTTP_200_OK) #converts the dict into JSON
    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data) #serializer: takes the incoming JSON data from the client
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #convert JSON to Object
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def task_details(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskList(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TaskDetails(APIView):
    def get(self,request,pk):
        task = get_object_or_404(Task,pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        task = get_object_or_404(Task,pk=pk)
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        task = get_object_or_404(Task,pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=['GET']) 
    #detail=False means it won't provide primary key.
    #detail=True-> has to pass pk
    def send_email(self,request):
        print("Sending an email...")
        return Response({"Message": "Email Sent"})

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UniversityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer