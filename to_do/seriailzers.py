from rest_framework import serializers

from to_do.models import ToDoList, ToDoItem


class DeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class ToDoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)

    def create(self, validated_data):
        todo_list = ToDoList(
            title=validated_data['title']
        )
        todo_list.save()

        return todo_list

    def to_representation(self, instance):
        todo_items = ToDoItem.objects.filter(todo_list=instance)
        representation = super().to_representation(instance)
        representation['items'] = ToDoItemSerializer(todo_items, many=True, context=self.context).data
        return representation


class ToDoItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    created_date = serializers.DateTimeField(read_only=True)
    due_date = serializers.DateTimeField(required=False)
    todo_list = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        todo_item = ToDoItem(
            title=validated_data['title'],
            description=validated_data['description'],
            due_date=validated_data.get('due_date', None),
            todo_list=validated_data.get('todo_list')
        )
        todo_item.save()

        return todo_item

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.todo_list = validated_data.get('todo_list', instance.todo_list)
        instance.save()

        return instance
