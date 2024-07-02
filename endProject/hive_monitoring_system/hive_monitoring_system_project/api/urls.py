from django.urls import path
from .views import (
    UserListView, PurchaseListView, ApiaryListView, HiveListView, 
    InspectionListView, ModuleListView, UserModuleListView, 
    SensorDataListView, ProductListView, UserProductListView
)
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('apiaries/', ApiaryListView.as_view(), name='apiary-list'),
    path('hives/', HiveListView.as_view(), name='hive-list'),
    path('inspections/', InspectionListView.as_view(), name='inspection-list'),
    path('modules/', ModuleListView.as_view(), name='module-list'),
    path('user-modules/', UserModuleListView.as_view(), name='user-module-list'),
    path('sensor-data/', SensorDataListView.as_view(), name='sensor-data-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('user-products/', UserProductListView.as_view(), name='user-product-list'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)