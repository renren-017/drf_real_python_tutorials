from django.urls import path

from blogs.views import CategoryView, CategoryDetailView, PostView, PostDetailView, PostCommentView, \
    PostCommentDetailView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='api-categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='api-category-detail'),

    path('', PostView.as_view(), name='api-posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='api-post-detail'),
    path('comment/', PostCommentView.as_view(), name='api-post-comment'),
    path('comment/<int:pk>/', PostCommentDetailView.as_view(), name='api-post-comment-detail'),

]
