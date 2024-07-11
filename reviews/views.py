from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from reviews.serializers import ReviewModelSerializer
from app.permissions import GlobalDefaultPermissions


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer

class ReviewDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer()