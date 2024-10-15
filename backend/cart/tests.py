import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import CartItem,Cart

from .serializers import CartSerializer, CartItemSerializer

from rest_framework import status 
# Create your tests here.

@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def cart_data():
    return {'cart':'New Cart'}
    
@pytest.fixture
def cartitem_data():
    return {'product':'price'
    
def test_cart_list_view(api_client):
    url = reverse ('cart-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_cartitem_create_view(api_client, cartitem_data):
    url = reverse ('cartitem-list')
    response = api_client.post(url, cartitem_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED

