from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Producto
from .serializer import ProductoSerializer


# Create your views here.
class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer