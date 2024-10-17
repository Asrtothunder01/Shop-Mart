from django.urls import path

from django.contrib import admin

from . import views

urlpatterns = [
  path('v1/', views.CustomUserListView.as_view(), name = 'CustomUser_list'),
  
  path('v2/', views.CustomUserCreateView.as_view(), name = 'CustomUser_create'),
]

