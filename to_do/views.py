from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from to_do.models import ToDoList, ToDoItem
from to_do.seriailzers import ToDoListSerializer, ToDoItemSerializer


class ToDoListView(APIView):

    @swagger_auto_schema(responses={200: ToDoListSerializer(many=True)},
                         operation_summary='Reads all To Do Lists')
    def get(self, request):
        todo_lists = ToDoList.objects.all()
        serializer = ToDoListSerializer(todo_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ToDoListSerializer,
                         operation_summary='Creates new To Do List')
    def post(self, request):
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ToDoListDetailView(APIView):

    @swagger_auto_schema(responses={200: ToDoListSerializer},
                         operation_summary='Reads a certain To Do List by pk')
    def get(self, request, pk):
        todo_list = ToDoList.objects.get(pk=pk)
        serializer = ToDoListSerializer(todo_list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary='Deletes a certain To Do List by pk')
    def delete(self, request, pk):
        todo_list = ToDoList.objects.get(pk=pk)
        todo_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ToDoListItemView(APIView):

    @swagger_auto_schema(request_body=ToDoItemSerializer(many=True),
                         operation_summary='Creates new To Do List Item')
    def post(self, request, pk):
        todo_list = ToDoList.objects.get(pk=pk)
        serializer = ToDoListSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save(todo_list=todo_list)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ToDoListItemDetailView(APIView):

    def get_object(self, pk):
        return ToDoItem.objects.get(pk=pk)

    @swagger_auto_schema(request_body=ToDoItemSerializer(),
                         operation_summary='Updates a certain To Do List Item')
    def put(self, request, pk):
        todo_list_item = self.get_object(pk)
        serializer = ToDoItemSerializer(todo_list_item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary='Deletes a certain To Do List Item by pk')
    def delete(self, request, pk):
        todo_list_item = self.get_object(pk)
        todo_list_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
