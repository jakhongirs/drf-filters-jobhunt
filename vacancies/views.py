from django.shortcuts import render
from .models import Vacancy
from .serializer import VacancySerializer, DetailVacancySerializer, CategorySerializer, RegionSerializer, \
    DistrictSerializer
from rest_framework import generics
from helpers.pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.

# ALL VACANCIES:
class AllVacanciesView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('status', 'region__slug', 'category')
    search_fields = ('title',)


# DETAIL VACANCY:
class DetailVacancyView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = DetailVacancySerializer
    pagination_class = CustomPagination
