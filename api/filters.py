import django_filters

from api.models import Produto, Categoria


class CategoriaFilterSet(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='contains')

    class Meta:
        model = Categoria
        fields = ['nome']


class ProdutoFilterSet(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='contains')
    descricao = django_filters.CharFilter(field_name='descricao', lookup_expr='contains')
    categoria = django_filters.CharFilter(field_name='categoria__id', lookup_expr='exact')

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria']
