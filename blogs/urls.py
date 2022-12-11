from django.urls import path

from blogs.views import CategoryView, CategoryDetailView, PostView, PostDetailView, CategoryPostView, PostCommentView, \
    PostCommentDetailView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='api-categories'),
    path('categories/delete/', CategoryDetailView.as_view(), name='api-categories'),

    path('posts/', PostView.as_view(), name='api-posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='api-post-detail'),
    path('posts/category/', CategoryPostView.as_view(), name='api-post-category'),
    path('posts/<int:post_pk>/comment', PostCommentView.as_view(), name='api-post-comment'),
    path('comment/<int:post_pk>/', PostCommentDetailView.as_view(), name='api-post-comment-detail'),

    path('posts/category/', CategoryPostView.as_view(), name='api-post-category'),

]
