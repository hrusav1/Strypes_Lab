from django.urls import path, re_path
from .views import index

urlpatterns = [
    path('', index),
    re_path(r'^.*', index, name='index'),
    path('<path:path>', index),
]