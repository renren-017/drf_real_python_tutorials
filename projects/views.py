from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectView(APIView):

    @swagger_auto_schema(responses={200: ProjectSerializer(many=True)},
                         operation_summary='Reads all Projects')
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectDetailView(APIView):

    @swagger_auto_schema(responses={200: ProjectSerializer()},
                         operation_summary='Reads certain Project by pk')
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
