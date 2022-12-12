from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Category, Post, Comment
from blogs.serializers import CategorySerializer, DeleteSerializer, PostSerializer, CommentSerializer


class CategoryView(APIView):

    @swagger_auto_schema(responses={200: CategorySerializer(many=True)},
                         operation_summary='Reads all Categories')
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailView(APIView):

    @swagger_auto_schema(responses={200: CategorySerializer()},
                         operation_summary='Reads posts by certain Category')
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostView(APIView):

    @swagger_auto_schema(responses={200: PostSerializer(many=True)},
                         operation_summary='Reads all Posts')
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):

    @staticmethod
    def get_object(pk):
        post = Post.objects.get(pk=pk)
        return post

    @swagger_auto_schema(responses={200: PostSerializer()},
                         operation_summary='Reads a certain Post')
    def get(self, request, pk):
        post = self.get_object(pk)

        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostCommentView(APIView):
    @swagger_auto_schema(request_body=CommentSerializer(),
                         operation_summary='Posting a comment on a certain Post')
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: DeleteSerializer()},
                         operation_summary='Deletes Comments by PK')
    def delete(self, request):
        delete_ids = [b['id'] for b in request.data]
        posts = Comment.objects.filter(id__in=delete_ids)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostCommentDetailView(APIView):

    @staticmethod
    def get_object(pk):
        return Comment.objects.get(pk=pk)

    @swagger_auto_schema(request_body=CommentSerializer, operation_summary='Updates a certain Post Comment')
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
