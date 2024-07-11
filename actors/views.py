from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializers import ActorModelSerializer
from app.permissions import GlobalDefaultPermissions



class ActorListCreateView(generics.ListCreateAPIView):
    # essa classe é uma das classes de permissão do DRF que indica que para acessar essa view é necessário estar autenticado
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    # informar queryset e serializer class
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer


class ActorDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer
