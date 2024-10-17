from django.contrib import admin

from django.urls import path

from . import views


urlpatterns = [
 path('v1/', views.PaymentListView.as_view(),name = 'payment_list'),
 
 path ('v2/', views.PaymentCreateView.as_view(), name = 'payment_create'),
]