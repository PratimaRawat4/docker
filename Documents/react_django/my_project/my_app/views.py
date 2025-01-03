from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price')
    max_price = filters.NumberFilter(field_name='price')
    brand = filters.CharFilter(field_name='brand')
    area = filters.CharFilter(field_name='area')
    year = filters.NumberFilter(field_name='year')
    category = filters.CharFilter(field_name='category')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'brand', 'area', 'year', 'category']



class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(name__icontains=search_query) | queryset.filter(description__icontains=search_query)
        return queryset







