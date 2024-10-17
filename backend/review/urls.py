from django.contrib import admin

from django.urls import path

from . import views


urlpatterns = [
 path('v1/', views.ReviewListView.as_view(),name = 'review_list'),
 
 path ('v2/', views.ReviewreateView.as_view(), name = 'review_create'),
 
]