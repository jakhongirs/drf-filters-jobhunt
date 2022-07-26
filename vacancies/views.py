from django.shortcuts import render
from .models import Vacancy
from .serializer import VacancySerializer, DetailVacancySerializer
from rest_framework import generics
from helpers.pagination import CustomPagination


# Create your views here.

# ALL VACANCIES:
class AllVacanciesView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    pagination_class = CustomPagination


# DETAIL VACANCY:
class DetailVacancyView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = DetailVacancySerializer
    pagination_class = CustomPagination
