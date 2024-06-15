from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list_create, name='companies'),
    path('watchlist/', views.watchlist_list_create, name='watchlist'),
    path('logout/', views.logout, name='logout'),
]
