from django.db import models
from helpers.models import BaseModel

# Create your models here.

# VACANCY STATUS CHOICES:
STANDARD = "STANDARD"
PREMIUM = "PREMIUM"
URGENT = "URGENT"

VACANCY_STATUS_CHOICES = (
    (STANDARD, "Standard"),
    (PREMIUM, "Premium"),
    (URGENT, "Urgent"),
)


# REGION:
class Region(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


# DISTRICT:
class District(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name


# CATEGORY:
class Category(BaseModel):
    slug = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)


# VACANCY:
class Vacancy(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    published_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    company_name = models.CharField(max_length=128)
    salary = models.IntegerField(default=0)
    status = models.CharField(max_length=128, choices=VACANCY_STATUS_CHOICES)

    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name='vacancies')
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True, related_name='vacancies')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return self.title
