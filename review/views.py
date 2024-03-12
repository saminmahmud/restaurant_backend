from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import viewsets

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
