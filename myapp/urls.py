from django.urls import path
from .views import temperature_humidity_api

urlpatterns = [
    path('temperature-humidity/', temperature_humidity_api, name='temperature_humidity_api'),
]
