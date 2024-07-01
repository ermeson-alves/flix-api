from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorModelSerializer


class ActorListCreateView(generics.ListCreateAPIView):
    # informar queryset e serializer class
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer


class ActorDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer
