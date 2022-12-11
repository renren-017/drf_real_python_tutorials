from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Category, Post, Comment
from blogs.serializers import CategorySerializer, DeleteSerializer, PostSerializer, CategoryPostSerializer, \
    CommentSerializer


class CategoryView(APIView):

    @swagger_auto_schema(responses={200: CategorySerializer(many=True)},
                         operation_summary='Reads all Categories')
    def get(self, request):
        projects = Category.objects.all()
        serializer = CategorySerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CategorySerializer(many=True),
                         operation_summary='Creates new Categories')
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    @swagger_auto_schema(responses={200: DeleteSerializer()},
                         operation_summary='Deletes Categories by PK')
    def delete(self, request):
        delete_ids = [b['id'] for b in request.data]
        categories = Category.objects.filter(id__in=delete_ids)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostView(APIView):

    @swagger_auto_schema(responses={200: PostSerializer(many=True)},
                         operation_summary='Reads all Posts')
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=PostSerializer(many=True),
                         operation_summary='Creates new Posts')
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: DeleteSerializer()},
                         operation_summary='Deletes Posts by PK')
    def delete(self, request):
        delete_ids = [b['id'] for b in request.data]
        posts = Post.objects.filter(id__in=delete_ids)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

    @swagger_auto_schema(request_body=PostSerializer, operation_summary='Updates a certain Post')
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryPostView(APIView):

    @swagger_auto_schema(request_body=CategoryPostSerializer(many=True),
                         operation_summary='Assigns Posts to Categories and vice versa')
    def post(self, request):
        serializer = CategoryPostSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: DeleteSerializer()},
                         operation_summary='Deletes Post <-> Category bond by Connection\'s PK')
    def delete(self, request):
        delete_ids = [b['id'] for b in request.data]
        posts = Post.objects.filter(id__in=delete_ids)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostCommentView(APIView):
    @swagger_auto_schema(request_body=CommentSerializer(),
                         operation_summary='Posting a comment on a certain Post')
    def post(self, request, post_pk):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post=post_pk)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_RpkEQUEST)


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

    @swagger_auto_schema(responses={200: DeleteSerializer()},
                         operation_summary='Deletes Comments by PK')
    def delete(self, request):
        delete_ids = [b['id'] for b in request.data]
        posts = Comment.objects.filter(id__in=delete_ids)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
