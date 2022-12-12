from rest_framework import serializers

from personal_diary.models import Entry


class EntrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    date_created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        entry = Entry(
            title=validated_data['title'],
            content=validated_data['content']
        )
        entry.save()

        return entry

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()

        return instance
