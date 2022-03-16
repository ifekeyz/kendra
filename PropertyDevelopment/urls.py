from django.urls import path

from .import views

urlpatterns = [
    path('property_development',views.property_development, name='property_development'),
]