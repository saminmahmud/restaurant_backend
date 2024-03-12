from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer