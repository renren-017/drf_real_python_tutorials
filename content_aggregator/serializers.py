from rest_framework import serializers


class EpisodeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()
    link = serializers.URLField()
    image = serializers.URLField()
    podcast_name = serializers.CharField(max_length=100)
    guid = serializers.CharField(max_length=500)
