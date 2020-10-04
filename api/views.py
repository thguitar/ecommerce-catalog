from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters import CategoriaFilterSet, ProdutoFilterSet
from api.models import Categoria, Produto
from api.serializers import CategoriaSerializer, ProdutoSerializer

# Create your views here.


class Index(APIView):
    def get(self, request):
        content = {"message": "Welcome to the Ecommerce Catalog API!"}
        return Response(content)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilterSet


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filterset_class = ProdutoFilterSet
