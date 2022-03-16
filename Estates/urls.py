from django.urls import path

from .import views

urlpatterns = [
    path('estates',views.estates, name='estates'),
]