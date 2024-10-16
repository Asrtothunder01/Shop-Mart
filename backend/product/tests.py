import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Product

from .serializers import ProductSerializer

from rest_framework import status 
# Create your tests here.

@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def discussion_data():
    return {'product':'New product'}
    
def test_product_list_view(api_client):
    url = reverse ('product-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_product_create_view(api_client, product_data):
    url = reverse ('product-list')
    response = api_client.post(url,product_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED

