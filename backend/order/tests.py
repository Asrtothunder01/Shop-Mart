import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Order, OrderItem

from .serializers import OrderSerializer, OrderItemSerializer

from rest_framework import status 
# Create your tests here.

@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def order_data():
    return {'order':'New order'}
    
def test_order_list_view(api_client):
    url = reverse ('order-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_order_create_view(api_client, order_data):
    url = reverse ('order-list')
    response = api_client.post(url,order_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED



@pytest.fixture
def orderitem_data():
    return {'orderitem':'New order'}
    
def test_orderitem_list_view(api_client):
    url = reverse ('order-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_orderitem_create_view(api_client, orderitem_data):
    url = reverse ('order-list')
    response = api_client.post(url,orderitem_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED

