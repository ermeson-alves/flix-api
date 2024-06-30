from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', views.MovieDetailUpdateDeleteView.as_view(), name='movie-detail'),
]