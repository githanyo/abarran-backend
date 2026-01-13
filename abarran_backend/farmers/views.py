from django.shortcuts import render
# farmers/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from .models import Farmer
from rest_framework import status
from .serializers import FarmerSerializer
from rest_framework.permissions import IsAuthenticated

class FarmerListView(ListAPIView):
    queryset = Farmer.objects.all().order_by("-registered_at")
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated]

class FarmerDetailView(RetrieveAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated]

class FarmerRegistrationView(APIView):
    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Registration successful"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
