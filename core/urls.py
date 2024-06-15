from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list, name='company-list'),
    path('watchlist/add/', views.add_to_watchlist, name='add-to-watchlist'),
]