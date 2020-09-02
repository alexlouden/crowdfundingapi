from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('shelters/', views.ShelterList.as_view()),
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('petcategories/', views.PetCategory.as_view()),
    path('<str:slug>/projects/', views.SheltersProjects.as_view()),
    path('<str:slug>/recommended/', views.RecommendedProjects.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)