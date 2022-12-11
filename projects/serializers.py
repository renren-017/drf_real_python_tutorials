from rest_framework import serializers

from projects.models import Project


class ProjectSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    technology = serializers.CharField(max_length=20)
    image = serializers.ImageField()

    def create(self, validated_data):
        project = Project(
            title=validated_data['title'],
            description=validated_data['description'],
            technology=validated_data['technology'],
            image=validated_data['image']
        )
        project.save()

        return project

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.technology = validated_data.get('technology', instance.technology)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance
