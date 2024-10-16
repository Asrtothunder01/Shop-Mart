from django.contrib import admin

from django.urls import path

from . import views


urlpatterns = [
 path('v1/', views.OrderListView.as_view(),name = 'order_list'),
 
 path ('v2/', views.OrderCreateView.as_view(), name = 'order_create'),
 
 path('v2/',views.OrderItemCreateView.as_view(), name = 'order_create'),
 
 path ('v1/', views.OrderItemListView.as_view(), name = 'order_list'),
]