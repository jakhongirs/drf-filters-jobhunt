from django.urls import path
from vacancies import views

urlpatterns = [
    path('vacancies/', views.AllVacanciesView.as_view(), name="all_vacancies"),
    path('vacancy/<int:pk>', views.DetailVacancyView.as_view(), name="detail_vacancy")
]
