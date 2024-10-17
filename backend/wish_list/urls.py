from . import views

from django.urls import path

from django.contrib import admin

urlpatterns = [
  path ('v1/', views.WishListView.as_view(), name = 'wishlist_list'),
  
  path('v2/', views.WishListCreateView.as_view(), name = 'wishlist_create'),
  
  path('v1/', views.WishListItemListView.as_view(), name = 'wishlist_item_list'),
  
  path('v2/', views.WishListItemCreateView.as_view(), name = 'wishlist_item_create'),

]