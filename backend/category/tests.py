import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Category

from .serializers import CategorySerializer

from rest_framework import status 
# Create your tests here.



@pytest.fixture
def category_data():
    return {'name':'New category'}
    
def test_category_list_view(api_client):
    url = reverse ('category-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_category_create_view(api_client,category_data):
    url = reverse ('category-list')
    response = api_client.post(url,category_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED

