from django.contrib import admin
from django.urls import path
from genres.views import genre_create_list_view, genre_detail_update_delete_view, \
GenreListCreateView, GenreDetailUpdateDeleteView
from actors.views import ActorListCreateView, ActorDetailUpdateDeleteView
from movies.views import MovieListCreateView, MovieDetailUpdateDeleteView
from reviews.views import ReviewListCreateView, ReviewDetailUpdateDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    # apenas django:
    path('genres-nodrf/', genre_create_list_view, name='genre-list-create-nodrf'),
    path('genres-nodrf/<int:pk>/', genre_detail_update_delete_view, name='genre-detail-nodrf'),
    # DRF:
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetailUpdateDeleteView.as_view(), name='genre-detail'),
    # actors urls:
    path('actors/', ActorListCreateView.as_view(), name='actor-list-create'),
    path('actors/<int:pk>/', ActorDetailUpdateDeleteView.as_view(), name='actor-detail'),
    # movies urls:
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailUpdateDeleteView.as_view(), name='movie-detail'),
    # reviews urls:
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailUpdateDeleteView.as_view(), name='review-detail'),
]
