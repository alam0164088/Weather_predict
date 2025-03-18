from django.urls import path
from .views import weather_view  # Ensure this line correctly imports the function

urlpatterns = [
    path('', weather_view, name='weather'),
]
