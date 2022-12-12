from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from flashcards.models import Card
from flashcards.serializers import CardSerializer, CardPatchSerializer


class CardView(APIView):
    box = openapi.Parameter('box', openapi.IN_QUERY,
                            description="Box Number [1-5]",
                            type=openapi.TYPE_STRING)

    def get_queryset(self, request):
        cards = Card.objects.all()
        box = request.query_params.get('box', None)
        if box is not None:
            cards = cards.filter(box=box)
        return cards

    @swagger_auto_schema(responses={200: CardSerializer(many=True)},
                         operation_summary='Reads all Flashcards',
                         manual_parameters=(box,))
    def get(self, request):
        cards = self.get_queryset(request)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CardSerializer,
                         operation_summary='Posts a new Flashcard')
    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CardDetailView(APIView):

    @staticmethod
    def get_object(pk):
        return Card.objects.get(pk=pk)

    @swagger_auto_schema(responses={200: CardSerializer},
                         operation_summary='Reads a Card by pk')
    def get(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CardSerializer,
                         operation_summary='Updates a certain Card by pk')
    def put(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(card, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CardPatchSerializer,
                         operation_summary='Partially updates a certain Card by pk')
    def patch(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(card, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary='Deletes a certain Card by pk')
    def delete(self, request, pk):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

