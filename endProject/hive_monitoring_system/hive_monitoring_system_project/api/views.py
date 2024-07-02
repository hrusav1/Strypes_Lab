from django.shortcuts import render
from rest_framework import generics
from .models import User, Purchase, Apiary, Hive, Inspection, Module, UserModule, SensorData, Product, UserProduct
from .serializers import (
    UserSerializer, PurchaseSerializer, ApiarySerializer, HiveSerializer, 
    InspectionSerializer, ModuleSerializer, UserModuleSerializer, 
    SensorDataSerializer, ProductSerializer, UserProductSerializer
)

#create your views here

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PurchaseListView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class ApiaryListView(generics.ListAPIView):
    queryset = Apiary.objects.all()
    serializer_class = ApiarySerializer

class HiveListView(generics.ListAPIView):
    queryset = Hive.objects.all()
    serializer_class = HiveSerializer

class InspectionListView(generics.ListAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

class ModuleListView(generics.ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class UserModuleListView(generics.ListAPIView):
    queryset = UserModule.objects.all()
    serializer_class = UserModuleSerializer

class SensorDataListView(generics.ListAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserProductListView(generics.ListAPIView):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializer