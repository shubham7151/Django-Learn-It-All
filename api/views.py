from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from student.models import Student
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee

# Create your views here.

@api_view(['GET', "POST"])
def studentsView(request):
    if request.method == "GET":
        student = Student.objects.all()
        serialiser = StudentSerializer(student, many = True)
        return Response(serialiser.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serialiser = StudentSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET', 'PUT'])
def studentDetailsView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = EmployeeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(serializer.error_messages, status=status.HTTP_500_INTERNAL_SERVER_ERROR)