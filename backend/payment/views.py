from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from .models import Payment

from .serializers import PaymentSerializer

from drf_spectacular.utils import extend_schema



@extend_schema(
 tags = ['Payment'],
 responses = {200: PaymentSerializer (many = True)},
)
class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    
    serializer_class = PaymentSerializer
    
    pagination_class = None
    
    permission_class = [IsAuthenticated]
    
@extend_schema(
 tags = ['Payment'],
 responses = {201: PaymentSerializer (many = True)},
)
class PaymentCreateView(CreateAPIView):
    queryset = Payment.objects.all()
    
    serializer_class = PaymentSerializer
    
    pagination_class = None
    
    permission_class = [IsAuthenticated]