from .serializers import CustomUserSerializer

from .models import CustomUser

from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema



@extend_schema(
  tags = ['CustomUser'],
  responses = {201: CustomUserSerializer (many = True)},
)
class CustomUserCreateView (CreateAPIView):
    queryset = CustomUser.objects.all()
    
    serializer_class = CustomUserSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
  
      
# CustomUser List View
  
@extend_schema(
  tags = ['CustomUser'],
  responses = {200: CustomUserSerializer (many = True)},
)  
class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    
    serializer_class = CustomUserSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    