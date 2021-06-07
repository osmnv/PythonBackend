
from rest_framework import viewsets, filters
from rest_framework import generics

from django_filters import rest_framework as dj_filters

from .serializers import AdSerializer, CategorySerializer
from .models import Ad, Category


class PriceFilter(dj_filters.FilterSet):
    min_price = dj_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = dj_filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_datetime = dj_filters.DateTimeFilter(field_name="pub_date", lookup_expr='gte')
    max_datetime = dj_filters.DateTimeFilter(field_name="pub_date", lookup_expr='lte')

    class Meta:
        model = Ad
        fields = ['price', 'pub_date']


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [dj_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PriceFilter
    search_fields = ['title']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer