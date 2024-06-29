from django.contrib import admin
from django.urls import path
from genres.views import genre_create_list_view, genre_detail_update_delete_view, \
GenreListCreateView, GenreDetailUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    # apenas django:
    path('genres/', genre_create_list_view, name='genre-list'),
    path('genres/<int:pk>/', genre_detail_update_delete_view, name='genre-detail'),
    # DRF:
    path('genres-drf/', GenreListCreateView.as_view(), name='genre-list-drf'),
    path('genres-drf/<int:pk>/', GenreDetailUpdateDeleteView.as_view(), name='genre-detail-drf'),

]
