from django.shortcuts import render
from rest_framework import viewsets

from movies.models import MovieData
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer
