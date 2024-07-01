import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreModelSerializer
# STATUS CODE: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


# COM DJANGO REST FRAMEWORK #############################################
class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


class GenreDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer



# APENAS COM DJANGO #############################################
@csrf_exempt # csrf token
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all() # SELECT * FROM genre;
        genres = [{'id': genre.id, 'name': genre.name} for genre in genres]
        # safe=False permite que listas também sejam serializadas;
        # DRF facilitaria se houvessem muitos campos na tabela;
        return JsonResponse(genres, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save() # INSERT new_genre INTO genre;
        return JsonResponse({'id': new_genre.id, 
                             'name': new_genre.name},
                             status=201) # status p/ CREATED
    

@csrf_exempt
def genre_detail_update_delete_view(request, pk):
    # SELECT * FROM Genre WHERER pk=pk;
    # genre = Genre.objects.get(pk=pk)
    genre = get_object_or_404(Genre, pk=pk) # tratamento para objeto não encontrado
    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {'id': genre.id, 'name': genre.name},
        )
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message': 'Gênero excluído!'},
            status=204, # status p/ No content
        )