from django.contrib.auth.models import User
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets, mixins
from .models import Products,Order,Employes
from .serializers import (
    ProductSerializer,
    OrderSerializer,
    EmployeSerializer,
    ProductDetailSerializer,
    OrderDetailSerializer,
    UserSerializer
)
from .services import ProductFilter


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProductListViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends =(DjangoFilterBackend, )
    filter_class = ProductFilter

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductDetailSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer


class EmployesListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Employes.objects.all()
    serializer_class = EmployeSerializer

class EmployeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employes.objects.all()
    serializer_class = EmployeSerializer

