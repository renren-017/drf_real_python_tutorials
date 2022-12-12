from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from content_aggregator.models import Episode
from content_aggregator.serializers import EpisodeSerializer


class EpisodeView(APIView):

    @swagger_auto_schema(responses={200: EpisodeSerializer(many=True)},
                         operation_summary='Reads all Real Python Podcast Episodes')
    def get(self, request):
        paginator = PageNumberPagination()
        episodes = paginator.paginate_queryset(Episode.objects.all(), request)
        serializer = EpisodeSerializer(episodes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
