from collections import OrderedDict

from rest_framework import serializers

from flashcards.models import Card


class CardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.CharField(max_length=100)
    answer = serializers.CharField(max_length=100)
    box = serializers.IntegerField(min_value=1, max_value=5)
    date_created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        card = Card(
            question=validated_data['question'],
            answer=validated_data['answer'],
            box=validated_data['box']
        )
        card.save()
        return card

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.box = validated_data.get('box', instance.box)
        instance.save()
        return instance


class CardPatchSerializer(CardSerializer):
    # Only for schema generation, not actually used.
    # because DRF-YASG does not support partial.
    def get_fields(self):
        new_fields = OrderedDict()
        for name, field in super().get_fields().items():
            field.required = False
            new_fields[name] = field
        return new_fields
