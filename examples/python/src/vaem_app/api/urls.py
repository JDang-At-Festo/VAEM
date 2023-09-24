from django.contrib import admin
from django.urls import path, include
from .views import vaem_status_view

urlpatterns = [
    path('api/', vaem_status_view.as_view())
]
