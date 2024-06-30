from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer): # herda de ModelSerializer
    class Meta:
        model = Movie
        fields = '__all__'
