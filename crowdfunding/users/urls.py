from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/supporter/', views.SupporterUserList.as_view()),
    path('users/supporter/<int:pk>/', views.SupporterUserDetail.as_view()),
    path('users/owner/', views.OwnerUserList.as_view()),
    path('users/owner/<int:pk>/', views.OwnerUserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)