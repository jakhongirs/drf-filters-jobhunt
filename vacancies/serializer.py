from rest_framework import serializers
from .models import Vacancy, Category, Region, District


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["name"]


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name']


class VacancySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    region = RegionSerializer()
    district = DistrictSerializer()

    class Meta:
        model = Vacancy
        fields = "__all__"


class DetailVacancySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    region = RegionSerializer()
    district = DistrictSerializer()

    class Meta:
        model = Vacancy
        fields = "__all__"
