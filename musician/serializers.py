from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer:
    is_adult = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        )

    def get_is_adult(self, obj):
        return obj.is_adult
