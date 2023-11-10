from django.urls import path

from . import views
from .models import Producto

urlpatterns = [
    path('api/productos/', views.ProductoList.as_view(), name='producto-list'),
    path('api/productos/<pk>/', views.ProductoDetail.as_view(), name='producto-detail'), 
]

