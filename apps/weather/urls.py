from django.contrib import admin
from django.urls import path
from .views import index, search_history_view

app_name = "weather"

urlpatterns = [
    path("", index, name="weather"),
    path('history/', search_history_view, name='history'),

]
