from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorListCreateView.as_view(), name='actor-list-create'),
    path('actors/<int:pk>/', views.ActorDetailUpdateDeleteView.as_view(), name='actor-detail'),
]