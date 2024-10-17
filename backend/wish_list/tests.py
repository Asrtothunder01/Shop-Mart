import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import WishList, WishListItem

from .serializers import WishListSerializer, WishListItemSerializer

from rest_framework import status 
# Create your tests here.

@pytest.fixture
def wishlistitem_data():
    return {'product':'paste'}

@pytest.fixture
def wishlist_data():
    return {'user':'dan'}
 
# Wish list   Test
def test_wishlist_list_view(api_client):
    url = reverse ('wishlist-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_wishlist_create_view(api_client,wishlist_data):
    url = reverse ('wishlist-list')
    response = api_client.post(url, wishlist_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED
    
    
# Wish List Item Test   
def test_wishlistitem_list_view(api_client):
    url = reverse ('wishlist_item-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_wishlistitem_create_view(api_client,wishlistitem_data):
    url = reverse ('wishlist_item-list')
    response = api_client.post(url,wishlistitem_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED

