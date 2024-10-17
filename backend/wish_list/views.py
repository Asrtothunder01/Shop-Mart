from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from .models import WishList, WishListItem

from .serializers import WishListSerializer, WishListItemSerializer

from drf_spectacular.utils import extend_schema


