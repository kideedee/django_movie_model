from rest_framework import serializers

from movies.models import MovieData


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = ['id', 'name', 'duration', 'rating', 'typ']
