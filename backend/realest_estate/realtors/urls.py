from django.urls import path, include
from .views import RealtorListView, RealtorView, TopSellerView

urlpatterns = [
    path('', RealtorListView.as_view()),
    path('topseller/', TopSellerView.as_view()),
    path('<pk>/', RealtorView.as_view()),
]