from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Products,Order,Employes
from .serializers import (
    ProductSerializer,
    OrderSerializer,
    EmployeSerializer,
    ProductDetailSerializer,
    OrderDetailSerializer
)

# Create your views here.

class ProductListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Products.objects.all()
    serializer_class = ProductDetailSerializer


class OrderListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer


class EmployesListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Employes.objects.all()
    serializer_class = EmployeSerializer

class EmployeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Employes.objects.all()
    serializer_class = EmployeSerializer