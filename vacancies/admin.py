from django.contrib import admin
from .models import Vacancy, Category, Region, District


# Register your models here.

# VACANCY
class VacancyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Vacancy, VacancyAdmin)


# CATEGORY:
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


# REGION:
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Region, RegionAdmin)


# DISTRICT:
class DistrictAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(District, DistrictAdmin)
