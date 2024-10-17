from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from .models import Review

from .serializers import  ReviewSerializer

from drf_spectacular.utils import extend_schema



@extend_schema(
 tags = ['Review'],
 responses = {200: ReviewSerializer (many = True)},
)
class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    
    serializer_class = ReviewSerializer
    
    pagination_class = None
    
    permission_class = [IsAuthenticated]
    
@extend_schema(
 tags = ['Review'],
 responses = {201: ReviewSerializer (many = True)},
)
class ReviewCreateView(ListAPIView):
    queryset = Review.objects.all()
    
    serializer_class = ReviewSerializer
    
    pagination_class = None
    
    permission_class = [IsAuthenticated]