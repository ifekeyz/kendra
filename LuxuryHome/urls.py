from django.urls import path

from .import views

urlpatterns = [
    path('luxury_homes',views.luxury_homes, name='luxury_homes'),
]