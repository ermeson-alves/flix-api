from rest_framework import serializers
from movies.models import Movie
from movies.models import Movie
from actors.models import Actor
from genres.models import Genre
from django.db.models import Avg


# class MovieSerializer(serializers.Serializer): # Serializer "puro"
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     release_date = serializers.DateField()
#     resume = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(
#         queryset=Genre.objects.all(),
#     )
#     actors = serializers.PrimaryKeyRelatedField(
#         queryset=Actor.objects.all(),
#         many=True,
#     )

class MovieModelSerializer(serializers.ModelSerializer): # herda de ModelSerializer
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj): 
        """Função para obter a média de estrelas de CADA filme, com Campos Calculados."""

        # reviews = obj.reviews.all() # permite obter todas as reviews de um obj (Movie); Movie é chave estrangeira de Reviews
        # if reviews:
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count = reviews.count()
        #     return round(sum_reviews / reviews_count, 1)

        # return None
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        
        return None

    def validate_release_date(self, value):
        if value.year < 1989:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior a 1989!')
        return value