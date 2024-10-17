import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import CustomUser

from .serializers import CustomUserSerializer

from rest_framework import status 
# Create your tests here.



@pytest.fixture
def customUser_data():
    return {'orde':'New order'}
    
def test_customuser_list_view(api_client):
    url = reverse ('customuser-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_customuser_create_view(api_client,customuser_data):
    url = reverse ('customuser-list')
    response = api_client.post(url,customuser_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED

