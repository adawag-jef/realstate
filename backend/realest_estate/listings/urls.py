from django.urls import path, include
from .views import ListingsView, ListingView, SearchView
urlpatterns = [
    path('', ListingsView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>', ListingView.as_view())
]