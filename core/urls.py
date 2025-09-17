from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Weather and shared endpoints
    path('weather/', views.WeatherView.as_view(), name='weather'),
    path('weather/alerts/', views.WeatherAlertsView.as_view(), name='weather-alerts'),
]