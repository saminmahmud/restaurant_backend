from django.shortcuts import render
from rest_framework import viewsets
from .models import Food
from .serializers import FoodSerializer

class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
