from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from personal_diary.models import Entry
from personal_diary.serializers import EntrySerializer


class EntryView(APIView):
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(responses={200: EntrySerializer(many=True)},
                         operation_summary='Reads all Diary Entries')
    def get(self, request):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=EntrySerializer,
                         operation_summary='Posts a new Diary Entry')
    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class EntryDetailView(APIView):
    permission_classes = (IsAdminUser,)

    @staticmethod
    def get_object(pk):
        return Entry.objects.get(pk=pk)

    @swagger_auto_schema(responses={200: EntrySerializer},
                         operation_summary='Reads a Diary Entry by pk')
    def get(self, request, pk):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=EntrySerializer,
                         operation_summary='Updates a certain Diary Entry')
    def put(self, request, pk):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary='Deletes a certain Diary Entry by pk')
    def delete(self, request, pk):
        entry = self.get_object(pk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

