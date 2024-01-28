from django.urls import path
from .views import add_restaurant, show_restaurants

urlpatterns = [
    path('add/', add_restaurant, name='add_restaurant'),
    path('', show_restaurants, name='show_restaurants'),
    # Добавьте другие URL-маршруты по мере необходимости
]