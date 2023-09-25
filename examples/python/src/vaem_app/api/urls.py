from django.contrib import admin
from django.urls import path, include
from .views import VaemStatusView, CurrentStateView

urlpatterns = [
    path('api/', VaemStatusView.as_view()),
    path('api/status/', CurrentStateView.as_view()),
]
