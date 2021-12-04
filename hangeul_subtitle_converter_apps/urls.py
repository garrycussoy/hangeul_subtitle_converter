# Import some packages needed
from django.contrib import admin
from django.urls import path, include
from . import views

# Define app name and url patterns
app_name = 'hangeul_subtitle_converter_apps'
urlpatterns = [
  path('', views.index, name = 'index'),
  path('contact', views.contact, name = 'contact'),
  path('watch', views.fetch_and_convert, name = 'fetch_and_convert')
]
