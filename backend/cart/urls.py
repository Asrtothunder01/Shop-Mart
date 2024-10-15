from django.urls import path

from django.contrib import admin

from . import views

urlpatterns = [

  path('v1/',views.CartListView.as_view(), name = 'Cart'),
  path ('v2/', views.CartCreateView.as_view(), name = 'Cart'),

]