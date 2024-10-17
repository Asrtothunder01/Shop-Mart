from django.urls import path

from django.contrib import admin

from . import views

urlpatterns = [
  path('v1/', views.CategoryListView.as_view(), name = 'category_list'),
  
  path('v2/', views.CategoryCreateView.as_view(), name = 'category_create'),
]

