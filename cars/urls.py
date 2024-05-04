from django.urls import path
from .views import get_info, get_cars, add_cars, detail, update_cars

app_name = 'cars'
urlpatterns = [
    path('', get_info, name='get_info'),
    path('cars/<int:pk>', get_cars, name='get_cars'),
    path('cars/detail/<int:pk>', detail, name='detail'),
    path('add_cars', add_cars, name='add_cars'),
    path('update_cars/<int:pk>/', update_cars, name='update_cars'),
]
