import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Review

from .serializers import ReviewSerializer

from rest_framework import status 
# Create your tests here.



@pytest.fixture
def review_data():
    return {'comment':'New order'}
    
def test_review_list_view(api_client):
    url = reverse ('review-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_review_create_view(api_client,review_data):
    url = reverse ('review-list')
    response = api_client.post(url,review_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED

