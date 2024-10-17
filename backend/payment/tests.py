import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Payment

from .serializers import PaymentSerializer

from rest_framework import status 
# Create your tests here.



@pytest.fixture
def payment_data():
    return {'amount':'100'}
    
def test_payment_list_view(api_client):
    url = reverse ('payment-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_payment_create_view(api_client, payment_data):
    url = reverse ('payment-list')
    response = api_client.post(url,payment_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED

