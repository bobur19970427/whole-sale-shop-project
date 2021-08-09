from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Products, Order, Employes


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class ProductDetailSerializer(serializers.ModelSerializer):
    color =serializers.SlugRelatedField(slug_field='name', read_only=True)
    sub_category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    brand = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Products
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
class OrderDetailSerializer(serializers.ModelSerializer):
    employe = serializers.SlugRelatedField(slug_field='name', read_only=True)
    customer = serializers.SlugRelatedField(slug_field='username', read_only=True)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = "__all__"

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employes
        fields = "__all__"