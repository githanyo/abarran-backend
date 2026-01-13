# farmers/urls.py
from django.urls import path
from .views import (FarmerRegistrationView, FarmerListView, FarmerDetailView,)

urlpatterns = [
    path('register/', FarmerRegistrationView.as_view()),
    path("list/", FarmerListView.as_view()),
    path("<int:pk>/", FarmerDetailView.as_view()),
]
