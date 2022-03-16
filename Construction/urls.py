from django.urls import path

from .import views

urlpatterns = [
    path('construction/',views.construction, name='construction'),
]