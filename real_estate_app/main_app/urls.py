from django.contrib import admin
from django.urls import path
from .views import predict

urlpatterns = [
    path('predict/', predict, name='predict'),
]