from django.contrib import admin
from django.urls import path, include
from actors.views import ActorListCreateView, ActorDetailUpdateDeleteView
from movies.views import MovieListCreateView, MovieDetailUpdateDeleteView
from reviews.views import ReviewListCreateView, ReviewDetailUpdateDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    # apenas django:
    # path('genres-nodrf/', genre_create_list_view, name='genre-list-create-nodrf'),
    # path('genres-nodrf/<int:pk>/', genre_detail_update_delete_view, name='genre-detail-nodrf'),

    # DRF:
    # path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    # path('genres/<int:pk>/', GenreDetailUpdateDeleteView.as_view(), name='genre-detail'),
    
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),
]
