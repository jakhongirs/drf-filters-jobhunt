from django.shortcuts import render
from .models import Vacancy
from .serializer import VacancySerializer, DetailVacancySerializer, CategorySerializer, RegionSerializer, \
    DistrictSerializer
from rest_framework import generics
from helpers.pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from django_filters import rest_framework


# Create your views here.
class CustomVacancyFilter(filters.BaseFilterBackend):
    min_price = rest_framework.NumberFilter(field_name="min_salary", lookup_expr='gte', label="Minimum salary")
    max_price = rest_framework.NumberFilter(field_name="max_salary", lookup_expr='lte', label="Maximum salary")

    created_at = rest_framework.DateTimeFromToRangeFilter(field_name='created_at', label="Created date range")


# ALL VACANCIES:
class AllVacanciesView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('status', 'region', 'region__slug', 'category')
    search_fields = ('title',)


# DETAIL VACANCY:
class DetailVacancyView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = DetailVacancySerializer
    pagination_class = CustomPagination
