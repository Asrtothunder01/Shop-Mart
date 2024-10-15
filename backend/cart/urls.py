from django.urls import path

from django.contrib import admin

from . import views

urlpatterns = [

  path('v1/',views.CartListView.as_view(), name = 'Cart'),
  path ('v2/', views.CartCreateView.as_view(), name = 'Cart'),
  
  path('v1/', views.CartItemListView.as_view(), name = 'CartItem'),
  
  path('v2/', views.CartItemCreateView.as_view(),name = 'CartItem'),


]