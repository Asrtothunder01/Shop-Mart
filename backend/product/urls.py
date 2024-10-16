from django.urls import path

from django.contrib import admin

from . import views

urlpatterns = [
  path('v1/', views.ProductListView.as_view(), name = 'product_list'),
  
  path('v2/', views.ProductCreateView.as_view(), name = 'product_create'),
]

