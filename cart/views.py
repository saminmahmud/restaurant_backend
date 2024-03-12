from django.shortcuts import render
from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer

class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
