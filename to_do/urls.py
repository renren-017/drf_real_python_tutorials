from django.urls import path

from to_do.views import ToDoListView, ToDoListItemView, ToDoListItemDetailView, ToDoListDetailView

urlpatterns = [
    path('list/', ToDoListView.as_view(), name='api-todolists'),
    path('list/<int:pk>/', ToDoListDetailView.as_view(), name='api-todolist-detail'),

    path('list/<int:pk>/item', ToDoListItemView.as_view(), name='api-todoitem-create'),
    path('item/<int:pk>/', ToDoListItemDetailView.as_view(), name='api-todoitem-detail'),
]
